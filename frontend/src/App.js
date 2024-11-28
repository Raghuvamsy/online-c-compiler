import React, { useState, useEffect } from 'react';
import * as monaco from 'monaco-editor';
import './App.css';

const App = () => {
  const [editor, setEditor] = useState(null);
  const [code, setCode] = useState('// Start coding in C\n#include<stdio.h>\nint main() {\n  printf("Hello, World!");\n  return 0;\n}');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);
  const [userInput, setUserInput] = useState(''); // State for user input

  const handleRun = async () => {
    setLoading(true);
    setOutput('');

    try {
      const response = await fetch(${process.env.REACT_APP_BACKEND_URL}/compile, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code, input: userInput }), // Send both code and input
      });

      const result = await response.json();
      if (response.ok) {
        setOutput(result.output);
      } else {
        setOutput(result.output || 'An error occurred while running the code.');
      }
    } catch (error) {
      setOutput('Failed to connect to the backend server.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const newEditor = monaco.editor.create(document.getElementById('editor'), {
      value: code,
      language: 'c',
      theme: 'vs-dark',
      automaticLayout: true,
    });

    newEditor.onDidChangeModelContent(() => {
      const updatedCode = newEditor.getValue();
      setCode(updatedCode);
    });

    setEditor(newEditor);

    // Cleanup editor instance on component unmount
    return () => {
      if (editor) editor.dispose();
    };
  }, []);

  return (
    <div className="app-container">
      <h1 className="app-title">Online C Compiler</h1>
      <div className="editor-container">
        <div id="editor" className="code-editor"></div>
      </div>
      <div className="input-container">
        <textarea
          placeholder="Enter input for your program"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          className="input-box"
        ></textarea>
      </div>
      <button className="run-button" onClick={handleRun} disabled={loading}>
        {loading ? 'Running...' : '▶️ Run Code'}
      </button>
      <div className="output-container">
        <h3>Output:</h3>
        <pre className="output">{output}</pre>
      </div>
    </div>
  );
};

export default App;

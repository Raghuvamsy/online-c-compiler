import React, { useState, useEffect } from 'react';
import * as monaco from 'monaco-editor';
import './App.css';  // Import the CSS file for styling

const App = () => {
  const [editor, setEditor] = useState(null);
  const [code, setCode] = useState('// Start coding in C\n#include<stdio.h>\nint main() {\n  printf("Hello, World!");\n  return 0;\n}');
  const [output, setOutput] = useState('');

  // Function to send code to the backend and run it when Play button is pressed
  const handleRun = async () => {
    try {
      const response = await fetch('https://online-c-compiler-r7fe.onrender.com', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code }),
      });
      const result = await response.json();
      setOutput(result.output); // Output or error message
    } catch (error) {
      setOutput('Failed to run the code.');
    }
  };

  useEffect(() => {
    const newEditor = monaco.editor.create(document.getElementById('editor'), {
      value: code,
      language: 'c',
      theme: 'vs-dark',
      automaticLayout: true,
    });

    // Update the state when the code in the editor changes
    newEditor.onDidChangeModelContent(() => {
      const updatedCode = newEditor.getValue();  // Get updated code
      setCode(updatedCode);                      // Update the state with the new code
    });

    setEditor(newEditor);
  }, []);

  return (
    <div className="app-container">
      <h1 className="app-title">Online C Compiler</h1>
      <div className="editor-container">
        <div id="editor" className="code-editor"></div>
      </div>
      <button className="run-button" onClick={handleRun}>▶️ Run Code</button>
      <div className="output-container">
        <h3>Output:</h3>
        <pre className="output">{output}</pre>
      </div>
    </div>
  );
};

export default App;

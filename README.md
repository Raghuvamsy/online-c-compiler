
# Online C Compiler

An **Online C Compiler** built using **React** for the frontend and hosted on **Vercel**, with the backend powered by **Node.js/Express** and deployed on **Render**. This tool allows users to write, compile, and run C programs directly in the browser.

---

## Features
- 🖋️ **Code Editor**: Built with [Monaco Editor](https://microsoft.github.io/monaco-editor/), providing syntax highlighting and an interactive coding experience.
- ▶️ **Run Code**: Executes C programs and displays output in real-time.
- 🌐 **Frontend & Backend Integration**: Seamless communication between the React frontend and Node.js backend.
- ⚡ **Fast and Responsive**: Optimized for a smooth coding experience.

---

## Demo
- **Frontend**: [Live Demo](https://online-c-compiler-three.vercel.app/)
- **Backend**: [Render API](https://online-c-compiler-z43z.onrender.com)

---

## Tech Stack
### **Frontend**
- [React](https://reactjs.org/) - Library for building user interfaces.
- [Monaco Editor](https://microsoft.github.io/monaco-editor/) - Code editor.

### **Backend**
- [Node.js](https://nodejs.org/) - JavaScript runtime.
- [Express](https://expressjs.com/) - Web framework for building REST APIs.

### **Hosting**
- **Frontend**: [Vercel](https://vercel.com/)
- **Backend**: [Render](https://render.com/)

---

## Installation and Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/Raghuvamsy/online-c-compiler.git
cd online-c-compiler
```

### **2. Setup Backend**
1. Navigate to the backend folder:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the server:
   ```bash
   npm start
   ```

### **3. Setup Frontend**
1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Create a `.env` file and add the backend URL:
   ```env
   REACT_APP_BACKEND_URL=https://online-c-compiler-z43z.onrender.com
   ```
4. Start the frontend:
   ```bash
   npm start
   ```

---

## How It Works
1. The user writes C code in the Monaco Editor.
2. When the "Run Code" button is clicked:
   - The code is sent to the backend `/compile` endpoint.
   - The backend uses a compiler (e.g., GCC) to execute the code and returns the output.
3. The output is displayed in the "Output" section.

---

## Future Improvements
- Add support for other programming languages (e.g., Python, Java).
- Improve error messages for debugging.
- Include features like input support, syntax checks, and dark mode.

---

## Contributing
Contributions are welcome!  
Feel free to fork the repository and submit a pull request.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Author
Developed by **Raghuvamsy** & **Brainitech**.  
GitHub Repository: [Online C Compiler](https://github.com/Raghuvamsy/online-c-compiler.git)

import logo from './logo.svg';
// import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./Pages/profile";
import About from "./Pages/dashboard";
function App() {
  return (
    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a>
    //   </header>
    // </div>
    
    <>
    {/* This is the alias of BrowserRouter i.e. Router */}
    <Router>
      <Routes>
      {/* This route is for home component 
          with exact path "/", in component props 
          we passes the imported component*/}
          <Route exact path="/" element={<Home/>} />
            
            {/* This route is for about component 
            with exact path "/aboxut", in component 
            props we passes the imported component*/}
            <Route path="/dashboard" element={<About/>} />
          
            {/* If any route mismatches the upper 
          route endpoints then, redirect triggers 
          and redirects app to home component with to="/" */}
          <Route to="/" />
      </Routes>
    </Router>
  </>

  );
}

export default App;

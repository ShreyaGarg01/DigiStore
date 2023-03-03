import logo from './logo.svg';
// import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./Pages/temp";
// import About from "./Pages/dashboard";
import Main from "./Pages/LandingPage";
import Profile from "./Pages/temp";

function App() {
  return (
    
    
    <>
    {/* <Main /> */}
    <Router>
      <Routes>
      
          <Route exact path="/" element={<Home/>} />
            
          <Route path="/profile" element={<Profile/>} />
            {/* <Route path="/dashboard" element={<About/>} /> */}
          
          <Route to="/" />
      </Routes>
    </Router>
  </>

  );
}

export default App;

import React from 'react';
import './main.css';

function Main() {
  return (
    <div class="container" onclick="onclick">
    <div class="top"></div>
    <div class="bottom"></div>
    <div class="center">
      <h2 class="head">App Name</h2>
      <a href=''>
        <button class="button">
           Shopkepper
        </button>
        
    </a>
    
    <a href=''>
        <button class="button">
           Customer
        </button>
    </a>
      
      <h2>&nbsp;</h2>
    </div>
  </div>
    )
}

export default Main;
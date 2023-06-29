import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Page from './components/Pages/Page';
import Login from './components/Forms/Users/Login';

function App(){

    return (
      <BrowserRouter>
          <Routes>
            <Route path="/" element={<Page />} />
            <Route path="/home" element={<Page />} />
            <Route path="/login" element={<Login />} />
          </Routes>
          
      </BrowserRouter>
    )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

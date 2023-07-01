import React, { useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Page from './components/Pages/Page';
import LoginPage from './components/Forms/Users/Login';
import SignupPage from './components/Forms/Users/Signup';

import Footer from './components/Pages/Footer';

import 'bootstrap/dist/css/bootstrap.css';

function App(){

    const pingGoogle = () => {
      fetch(`/ping/google`)
          .then(response => (response.ok ? console.log("Internet Conected") : console.log("Internet Disconected")))
          .catch(error => console.error("Error: ", error))
    }

    useEffect(() => {
      // Check Internet Connection
      // setInterval(pingGoogle, 1000);
    }, [])

    return (
      <div>
        <BrowserRouter>
            <Routes>
              <Route path="/" element={<Page />} />
              <Route path="/home" element={<Page />} />
              <Route path="/login" element={<LoginPage />} />
              <Route path="/signup" element={<SignupPage />} />
            </Routes>
            <Footer />
        </BrowserRouter>
      
      </div>
      
    )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

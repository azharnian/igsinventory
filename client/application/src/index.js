import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Page from './components/Pages/Page';
import LoginPage from './components/Forms/Users/Login';
import SignupPage from './components/Forms/Users/Signup';
import Footer from './components/Pages/Footer';
import Dashboard from './components/Pages/Dashboard';
import UserTypeForm from './components/Forms/Users/UserTypeForm';

import 'bootstrap/dist/css/bootstrap.css';

function App(){

    const [state, setState] = useState({
      title : "Ignatius Global School Inventory System"
    })

    const pingGoogle = () => {
      fetch(`/ping/google`)
          .then(response => (response.ok ? console.log("Internet Conected") : console.log("Internet Disconected")))
          .catch(error => console.error("Error: ", error))
    }

    useEffect(() => {
      document.title = state.title;
      // Check Internet Connection
      // setInterval(pingGoogle, 1000);
    }, [state.title])

    return (
      <div>
        <BrowserRouter>
            <Routes>
              <Route element={<Page title={state.title}/>}>
                <Route path="/" element={<Dashboard />} />
                <Route path="/user-type" element={<UserTypeForm />} />
              </Route>
              <Route path="/login" element={<LoginPage title={state.title}/>} />
              <Route path="/signup" element={<SignupPage title={state.title}/>} />
            </Routes>
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

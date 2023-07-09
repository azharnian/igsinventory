import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import PrivateRoute from './utils/PrivateRoute';

import Page from './components/Pages/Page';
import LoginPage from './components/Forms/Users/Login';
import SignupPage from './components/Forms/Users/Signup';
import Dashboard from './components/Pages/Dashboard';
import UserTypeForm from './components/Forms/Users/UserTypeForm';

import 'bootstrap/dist/css/bootstrap.css';
import NotFound from './components/Error/NotFound.jsx';
import { AuthProvider } from './context/AuthContext';

function App(){

    const [state, setState] = useState({
      title : "Ignatius Global School Inventory System",
      logged : false
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
    }, [])

    return (
      <div>
        <BrowserRouter>
          <AuthProvider>
          <Routes>
              <Route element={<PrivateRoute />}>
                    <Route path="/" element={<Dashboard />} />
                    <Route path="/user-type" element={<UserTypeForm />} />
              </Route> 
              <Route path="/login" element={<LoginPage title={state.title}/>} />
              <Route path="/signup" element={<SignupPage title={state.title}/>} />

              <Route path="*" element={<NotFound />} />
            </Routes>
          </AuthProvider>
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

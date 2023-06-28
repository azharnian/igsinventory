import React from 'react';
import ReactDOM from 'react-dom/client';
import Page from './components/Pages/Page';

function App(){

    return (
        <div>
           <Page />
        </div>
    )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

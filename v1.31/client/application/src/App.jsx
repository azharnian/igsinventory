import { BrowserRouter, Routes, Route } from 'react-router-dom'

import SignUpPage from './components/Pages/SignUpPage'
import LogInPage from './components/Pages/LogInPage'
import Dashboard from './components/Pages/DashboardPage'


import './App.css'

function App() {

  return (
    <>
     <BrowserRouter>
      <Routes>
        <Route path='/login' element={ <LogInPage /> } />
        <Route path='/signup' element={ <SignUpPage/> }  />
        <Route path='/dashboard' element={ <Dashboard/> }  />
      </Routes>
     </BrowserRouter>
    </>
  )
}

export default App

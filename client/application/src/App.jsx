import { BrowserRouter, Routes, Route } from 'react-router-dom'

import SignUpPage from './components/pages/SignUpPage'
import LogInPage from './components/pages/LogInPage'


import './App.css'

function App() {

  return (
    <>
     <BrowserRouter>
      <Routes>
        <Route path='/login' element={ <LogInPage /> } />
        <Route path='/signup' element={ <SignUpPage/> }  />
      </Routes>
     </BrowserRouter>
    </>
  )
}

export default App

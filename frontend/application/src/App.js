import React from 'react';
import Header from './components/Header/Header'
import MainPage from './components/ContentPage/MainPage/MainPage'
import SignUpPage from './components/Forms/SignUpPage/SignUpPage';
import LoginPage from './components/Forms/LoginPage/LoginPage';

class App extends React.Component {

    render = () => {
      return (
        <div className='app-wrapper'>
          <Header />
          {/* <MainPage /> */}
          {/* <SignUpPage /> */}
          < LoginPage/>
        </div>
      )
    }
}

export default App;

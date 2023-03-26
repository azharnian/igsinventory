import React from 'react';
import Header from './components/Header/Header'
import MainPage from './components/ContentPage/MainPage/MainPage'
import SignUpPage from './components/Forms/SignUpPage/SignUpPage';
import LoginPage from './components/Forms/LoginPage/LoginPage';

class App extends React.Component {

    constructor(props){
      super(props);
      this.state = {
        currentPage : "login"
      };
    }

    render = () => {
      return (
        <div className='app-wrapper'>
          <Header />
          { this.state.currentPage === "" ? (<MainPage />) : ""}
          { this.state.currentPage === "register" ? (<SignUpPage />) : "" }
          { this.state.currentPage === "login" ? (<LoginPage/>) : "" }
        </div>
      )
    }
}

export default App;

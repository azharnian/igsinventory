import React from 'react';
import Header from './components/Header/Header'
import MainPage from './components/ContentPage/MainPage/MainPage'

class App extends React.Component {

    render = () => {
      return (
        <div className='app-wrapper'>
          <Header />
          <MainPage />
        </div>
      )
    }
}

export default App;

import React from 'react'
import './MainPage.css'
import Navigation from '../Navigation/Navigation'

class MainPage extends React.Component {

    render = () => {
        return (
            <div className='container-main-page'>
                <Navigation />
            </div>
        )
    }

}

export default MainPage;
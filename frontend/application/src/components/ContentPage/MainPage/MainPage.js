import React from 'react'
import './MainPage.css'
import Navigation from '../Navigation/Navigation'
import BuildingEntryForm from '../../Forms/BuildingEntryForm/BuildingEntryForm'

class MainPage extends React.Component {

    render = () => {
        return (
            <div className='container-main-page'>
                <Navigation />
                <div className="container--content--main--page">
                    {/* <BuildingEntryForm /> */}
                </div>
            </div>
        )
    }

}

export default MainPage;
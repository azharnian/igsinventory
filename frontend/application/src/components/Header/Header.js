import React from 'react';
import './Header.css';
import logo from './images/logo.svg'

class InformationHeader extends React.Component {

    render = () => {
        return (
            <div className='information-header'>

            </div>
        )
    }

}

class MainHeader extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            companyName : 'ignatius global school',
            companyLogoSource : logo,
            userName : 'anas azhar',
            userPictureSource : logo
        };
    }

    render = () => {
        return (
            <div className='container-header'>
                <div className='main-header'>
                    <div className='logo-company-header'>
                        <div className='logo-box-header'>
                            <img src={this.state.companyLogoSource} alt={this.state.companyName} />
                        </div>
                        <span className='logo-text-header'>
                            {this.state.companyName} - Inventory
                        </span>
                    </div>
                    <div className='profile-picture-header'>
                        <span className='picture-text-header'>
                            {this.state.userName}
                        </span>
                        <div className='picture-box-header'>
                            <img src={this.state.userPictureSource} alt={this.state.userName} />
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

class Header extends React.Component {
    render = () => {
        return (
            <header>
                <InformationHeader />
                <MainHeader />
            </header>
        )
    }
}

export default Header;
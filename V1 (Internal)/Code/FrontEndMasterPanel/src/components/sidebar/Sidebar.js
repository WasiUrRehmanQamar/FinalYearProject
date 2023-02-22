import React, { useContext } from 'react'
import './sidebar.scss'
import DashboardIcon from "@mui/icons-material/Dashboard";
import PersonOutlineIcon from "@mui/icons-material/PersonOutline";
import LocalShippingIcon from "@mui/icons-material/LocalShipping";
import CreditCardIcon from "@mui/icons-material/CreditCard";
import StoreIcon from "@mui/icons-material/Store";
import InsertChartIcon from "@mui/icons-material/InsertChart";
import SettingsApplicationsIcon from "@mui/icons-material/SettingsApplications";
import ExitToAppIcon from "@mui/icons-material/ExitToApp";
import NotificationsNoneIcon from "@mui/icons-material/NotificationsNone";
import SettingsSystemDaydreamOutlinedIcon from "@mui/icons-material/SettingsSystemDaydreamOutlined";
import PsychologyOutlinedIcon from "@mui/icons-material/PsychologyOutlined";
import AccountCircleOutlinedIcon from "@mui/icons-material/AccountCircleOutlined";
import { Link } from 'react-router-dom'
import { DarkModeContext } from "../../context/darkModeContext";
const Sidebar = () => {
    const { dispatch } = useContext(DarkModeContext);
    return (
        <div className='sidebar'>
            <div className='top'>
                <Link to='/' style={{ textDecoration: "none" }}>
                    <span className='logo'>
                        Master Panel
                    </span>
                </Link>
            </div>
            <hr />
            <div className='center'>
                <ul>
                    <p className='title'>MAIN</p>
                    <Link to='/' style={{ textDecoration: "none" }}>
                        <li>
                            <DashboardIcon className='icon' />
                            <span>Dashboard</span>
                        </li>
                    </Link>
                    <p className='title'>LISTS</p>
                    <Link to='/users' style={{ textDecoration: "none" }}>
                        <li>
                            <PersonOutlineIcon className='icon' />
                            <span> Admin</span>
                        </li>
                    </Link>
                    <Link to='/Campus' style={{ textDecoration: "none" }}>
                        <li>
                            <StoreIcon className='icon' />
                            <span> Campus</span>
                        </li>
                    </Link>
                    <li>
                        <CreditCardIcon className='icon' />
                        <span> Department</span>
                    </li>
                    {/* <li>
                        <LocalShippingIcon className='icon' />
                        <span></span>
                    </li> */}
                    {/* <p className='title'>Socities</p> */}
                    <li>
                        <InsertChartIcon className='icon' />
                        <span> Socities</span>
                    </li>
                    <li>
                        <NotificationsNoneIcon className='icon' />
                        <span>Websites</span>
                    </li>
                    {/* <p className='title'>SERVICE</p> */}
                    <li>
                        <SettingsSystemDaydreamOutlinedIcon className='icon' />
                        <span>Event</span>
                    </li>
                    <li>
                        <SettingsApplicationsIcon className='icon' />
                        <span>Groups</span>
                    </li>
                    <li>
                        <PsychologyOutlinedIcon className='icon' />
                        <span>Menu</span>
                    </li>
                  
                    <p className='title'>USER</p>
                    {/* <li>
                        <AccountCircleOutlinedIcon className='icon' />
                        <span>Profile</span>
                    </li> */}
                    <li>
                        <ExitToAppIcon className='icon' />
                        <Link to="/" style={{textDecoration:"none"}}><span>Logout</span></Link>
                    </li>
                </ul>
            </div>
            <div className='bottom'>
                <div
                    className="colorOption"
                    onClick={() => dispatch({ type: "LIGHT" })}
                ></div>
                <div
                    className="colorOption"
                    onClick={() => dispatch({ type: "DARK" })}
                ></div>
            </div>
        </div>
    )
}


export default Sidebar
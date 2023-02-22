import React from 'react'
import './widgets.scss'
import KeyboardArrowUpIcon from "@mui/icons-material/KeyboardArrowUp";
import PersonOutlinedIcon from "@mui/icons-material/PersonOutlined";
import AccountBalanceWalletOutlinedIcon from "@mui/icons-material/AccountBalanceWalletOutlined";
import ShoppingCartOutlinedIcon from "@mui/icons-material/ShoppingCartOutlined";
import MonetizationOnOutlinedIcon from "@mui/icons-material/MonetizationOnOutlined";
import { Link } from 'react-router-dom';
const Widgets = ({ type }) => {
    let data;
    let amount = 2;
    let diff = 20;
    let link = "/users/new"
    switch (type) {
        case "campus":
            data = {
                title: "CAMPUS",
                isMoney: false,
                link: <b>Add new Campus</b>,
                icon: (
                    <PersonOutlinedIcon
                        className="icon"
                        style={{
                            color: "crimson",
                            backgroundColor: "rgba(255, 0, 0, 0.2)",
                        }}
                    />
                ),
            };
            break;
        case "department":
            data = {
                title: "DEPARTMENT",
                isMoney: false,
                link: "Add new Department",
                icon: (
                    <ShoppingCartOutlinedIcon
                        className="icon"
                        style={{
                            backgroundColor: "rgba(218, 165, 32, 0.2)",
                            color: "goldenrod",
                        }}
                    />
                ),
            };
            break;
        case "society":

            data = {
                title: "SOCIETY",
                isMoney: true,
                link: "Add new Society",
                icon: (
                    <MonetizationOnOutlinedIcon
                        className="icon"
                        style={{ backgroundColor: "rgba(0, 128, 0, 0.2)", color: "green" }}
                    />
                ),
            };
            break;
        case "admin":
            data = {
                title: "ADMIN",
                isMoney: true,
                link: "Add new Admin    ",
                icon: (
                    <AccountBalanceWalletOutlinedIcon
                        className="icon"
                        style={{
                            backgroundColor: "rgba(128, 0, 128, 0.2)",
                            color: "purple",
                        }}
                    />
                ),
            };
            break;
            
        case "website":

            data = {
                title: "WEBSITE",
                isMoney: true,
                link: "Add new Website",
                icon: (
                    <MonetizationOnOutlinedIcon
                        className="icon"
                        style={{ backgroundColor: "rgba(0, 128, 0, 0.2)", color: "green" }}
                    />
                ),
            };
            break;
            
        case "event":

            data = {
                title: "EVENT",
                isMoney: true,
                link: "Add new Event",
                icon: (
                    <MonetizationOnOutlinedIcon
                        className="icon"
                        style={{ backgroundColor: "rgba(0, 128, 0, 0.2)", color: "green" }}
                    />
                ),
            };
            break;
            
            
            case "menu":

            data = {
                title: "MENU",
                isMoney: true,
                link: "Add new Menu",
                icon: (
                    <MonetizationOnOutlinedIcon
                        className="icon"
                        style={{ backgroundColor: "rgba(0, 128, 0, 0.2)", color: "green" }}
                    />
                ),
            };
            break;

        case "goups":

            data = {
                title: "GROUPS",
                isMoney: true,
                link: "Add new Groups",
                icon: (
                    <MonetizationOnOutlinedIcon
                        className="icon"
                        style={{ backgroundColor: "rgba(0, 128, 0, 0.2)", color: "green" }}
                    />
                ),
            };
            break;
        default:
            break;
    }
    return (
        <div className='widget'>
            <div className='left'>
                <span className='title'>{data.title}</span>
                <span className='counter'> {amount}</span>
                <span className='link'><Link to={link} style={{textDecoration:"none",color:"black"}}><b>{data.link}</b></Link></span>
            </div>
            {/* <div className='right'>
                <div className='percentage positive'>
                    <KeyboardArrowUpIcon />
                    {diff} %
                </div>
                {data.icon}
            </div> */}
        </div>
    )
}

export default Widgets
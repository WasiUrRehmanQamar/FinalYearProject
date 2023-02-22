import React from 'react'
import './home.scss'
import Sidebar from '../../components/sidebar/Sidebar'
import Navbar from '../../components/navbar/Navbar'
import Widgets from '../../components/widgets/Widgets'
import Charts from '../../components/charts/Charts'
import Featured from '../../components/featured/Featured'
import Table from '../../components/table/Table'
const Home = () => {

    return (
        <div className='home'>
            <Sidebar />
            <div className='homeContainer'>
                <Navbar />
                <div className='widgets'>
                    <Widgets type="campus" />
                    <Widgets type="department" />
                    <Widgets type="society" />
                    <Widgets type="admin" />
                </div>

                <div className='widgets'>
                    <Widgets type="website" />
                    <Widgets type="event" />
                    <Widgets type="menu" />
                    <Widgets type="goups" />
                </div>
                
                {/* <div className='charts'>
                    <Featured />
                    <Charts title="Last 6 Months (Revenue)" aspect={2 / 1} />
                </div> */}
                {/* <div className='listContainer'>
                    <div className='listTitle'>Latest Transactions</div>
                    <Table />
                </div> */}
            </div>
        </div>
    )
}

export default Home
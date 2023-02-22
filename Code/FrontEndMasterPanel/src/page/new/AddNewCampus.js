import React, { useState } from 'react'
import './new.scss'
import Sidebar from '../../components/sidebar/Sidebar'
import Navbar from '../../components/navbar/Navbar'
import DriveFolderUploadOutlinedIcon from "@mui/icons-material/DriveFolderUploadOutlined";
const AddNewCampus = ({ inputs, title }) => {
    const [file, setFile] = useState("")
    
    return (
        <div className='new'>
            <Sidebar />
            <div className='newContainer'>
                <Navbar />
                <div className='top'>
                    {title}
                </div>
                <div className='bottom'>
                    {/* <div className='left'>
                        <img
                            src={
                                file
                                    ? URL.createObjectURL(file)
                                    : "https://icon-library.com/images/no-image-icon/no-image-icon-0.jpg"
                            }
                            alt=""
                        />
                    </div> */}
                    <div className='right'>
                        <form>
                            {/* <div className='formInput'>
                                <label htmlFor='file'>
                                    Image: <DriveFolderUploadOutlinedIcon className='icon' />
                                </label>
                                <input
                                    type='file' id='file'
                                    onChange={(e) => setFile(e.target.files[0])}
                                    style={{ display: "none" }} />
                            </div> */}
                            {/* {inputs.map((input) => ( */}
                            <div className="formInput" >
                                <label>Campus Name</label>
                                <input placeholder="Campus Name" />
                            </div>
                            <div className="formInput" >
                                <label>Campus Short Name</label>
                                <input placeholder="Campus Short Name" />
                            </div>
                            <div className="formInput" >
                                <label>Campus Address</label>
                                <input placeholder="Campus Address" />
                            </div>
                            <div className="formInput" >
                                <label>Campus Phone</label>
                                <input placeholder="Campus Phone" />
                            </div>
                            <div className="formInput" >
                                <label>Email</label>
                                <input placeholder="Email" />
                            </div>
                          
                            <div className="formInput" >
                                {/* <label>Email</label>
                                <input placeholder="Add new campus" /> */}
                            </div>

                            {/* // ))} */}
                            <button>Add</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default AddNewCampus
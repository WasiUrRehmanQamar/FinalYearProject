import React, { useContext } from 'react'
import './style/dark.scss'
import Home from './page/home/Home'
import Login from './page/login/Login'
import List from './page/list/List'
import SinglePage from './page/single/Single'
import AddNewCampus from './page/new/AddNewCampus'
import { productInputs, userInputs } from "./formSource";
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { DarkModeContext } from "./context/darkModeContext";
const App = () => {
  const { darkMode } = useContext(DarkModeContext);
  return (
    <div className={darkMode ? "app dark" : "app"}>
      <BrowserRouter>
        <Routes>
          <Route path="/">
          <Route index element={<Login />} />
            <Route path="Dashboard" index element={<Home/>} />
            <Route path='users'>
              <Route index element={<List />} />
              <Route path=':userId' element={<SinglePage />} />
              <Route path='new' element={<AddNewCampus inputs={userInputs} title="Add New Campuss" />} />
            </Route>
            <Route path='Campus'>
              <Route index element={<List />} />
              <Route path=':productId' element={<SinglePage />} />
              <Route path='new' element={<AddNewCampus inputs={productInputs} title="Add New Product" />} />
            </Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
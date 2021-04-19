
import React, {useState, useEffect} from 'react';
import { Layout, Menu, Breadcrumb } from 'antd';

import { enquireScreen } from 'enquire-js';
import 'antd/dist/antd.css';
const { Header, Content, Footer } = Layout;

import Navbar from "./Navbar.js"

import Banner2 from './Banner2';

import { Banner20DataSource } from './supplementary/data.source';

import './less/antMotionStyle.less';

let isMobile;

enquireScreen((b) => {
  isMobile = b;
});

const { location = {} } = typeof window !== 'undefined' ? window : {};

export const Home =(props)=> {

  const [isMobile, setisMobile]=useState();
  const [dom ,setDom] =useState();
  const[show , setShow] = useState(false);

    enquireScreen((b) => {
      setisMobile(b);
    });

  useEffect(() =>{

    enquireScreen((b) => {
      setisMobile(!!b);
    });

    if (location.port) {
      // 样式 build 时间在 200-300ms 之间; stle build is betwee 200 and 300 ms in between
      setTimeout(() => {
        setShow(true)
      }, 500);
    }

  })
  
    const children = [
      <Navbar/>, 
      <Banner2
        id="Banner2_0"
        key="Banner2_0"
        dataSource={Banner20DataSource}
        isMobile={isMobile}
      />

    ]

    return (
      <div
        className="templates-wrapper"
        ref={(d) => {
         setDom(d);
        }}
      > 
        {children} 
      </div>
    );

}

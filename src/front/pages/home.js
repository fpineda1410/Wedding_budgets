import React, {useState, useEffect} from 'react';
import { enquireScreen } from 'enquire-js';
import ReactDOM from 'react-dom';
import Nav3 from './Nav3.js';

import {
  Nav30DataSource
} from './support_files/data.source';

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
      <Nav3
        id="Nav3_0"
        key="Nav3_0"
        dataSource={Nav30DataSource}
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

// export default Home;
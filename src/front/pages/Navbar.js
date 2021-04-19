import React from 'react'
import { Layout, Menu, Row, Col,Button,Typography,PageHeader,Image } from 'antd';
import './css/navbar.css';
const { Header, Content, Footer } = Layout;

const { Title } = Typography;

function Navbar () {
  return (
    
    
     
      <Row style={{height:"10vh"}}>
          <Col span={6} xs={{ order: 1 }} sm={{ order: 2 }} md={{ order: 3 }} lg={{ order: 4 }}>
            <Button className="navbar_buttons" type="primary" ><Title level={5}>h2. Ant Design</Title></Button>
            <Button className="navbar_buttons" type="primary" ><Title level={5}>h2. Ant Design</Title></Button>
          </Col>
          <Col span={6} xs={{ order: 2 }} sm={{ order: 1 }} md={{ order: 4 }} lg={{ order: 3 }}>
            
          </Col>
          <Col span={6} xs={{ order: 3 }} sm={{ order: 4 }} md={{ order: 2 }} lg={{ order: 2 }}>
            
          </Col>
          <Col span={6} xs={{ order: 4 }} sm={{ order: 3 }} md={{ order: 1 }} lg={{ order: 1 }}>
          <Image
            className="logo"
            style={{marginTop:"1.5vh",marginLeft:"10vh"}}
            width={80}
            src="https://upload.wikimedia.org/wikipedia/commons/d/d6/Official_Logo_OneLove.png"
            />
          </Col>
      </Row>
     
       
      
   
  )
}

export default Navbar;
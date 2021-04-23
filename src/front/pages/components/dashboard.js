import React,{useContext,useEffect} from "react";

import "antd/dist/antd.css";
import "../css/dashboard.css";
import { Layout, Menu, Image } from "antd";
import {
  GiftTwoTone,
  BankTwoTone,
  CameraTwoTone,
  CameraOutlined,
  IdcardTwoTone,
  PhoneTwoTone,
  WalletTwoTone
} from "@ant-design/icons";

import { Statistic, Row, Col } from "antd";
import { LikeOutlined } from "@ant-design/icons";

const { SubMenu } = Menu;
const { Header, Content, Footer, Sider } = Layout;

import { Context } from "../../store/appContext.js";


export const Dashboard =()=> {
    const { store, actions } = useContext(Context);
    useEffect (()=>{
        actions.information_sorting_generator_flowers();
        actions.information_sorting_generator_locations();
        actions.information_sorting_generator_photo();
    },[])

    return (
    <Layout>
    <Header className="header">
      <div className="logo" />
      <Menu
        theme="dark"
        mode="horizontal"
        defaultSelectedKeys={["0"]}
        style={{ float: "right" }}
      >
        <Menu.Item key="1" >
          <IdcardTwoTone /> Registro
        </Menu.Item>
        <Menu.Item key="2">
          <WalletTwoTone />
          CheckOut
        </Menu.Item>
        <Menu.Item key="3">
          <PhoneTwoTone /> Contactenos
        </Menu.Item>
      </Menu>
    </Header>
    <Content style={{ padding: "0 50px" }}>
      {/* <Breadcrumb style={{ margin: '16px 0' }}>
        <Breadcrumb.Item>Home</Breadcrumb.Item>
        <Breadcrumb.Item>List</Breadcrumb.Item>
        <Breadcrumb.Item>App</Breadcrumb.Item>
      </Breadcrumb> */}
      <Layout className="site-layout-background" style={{ padding: "24px 0" }}>
        <Sider className="site-layout-background" width={200}>
          <Menu
            mode="inline"
            // defaultSelectedKeys={["0"]}
            // defaultOpenKeys={["sub1"]}
            style={{ height: "100%" }}
          >
            <SubMenu key="sub1" icon={<BankTwoTone />} title="Lugares">
              <Menu.Item key="1"onClick={()=>console.log(actions.information_sorting_generator_photo())}>Windham Herradura</Menu.Item>
              <Menu.Item key="2">Occidental Papagayo</Menu.Item>
              <Menu.Item key="3">Swiss Travel</Menu.Item>
              <Menu.Item key="4">Sheraton Escazu</Menu.Item>
            </SubMenu>
            <SubMenu key="sub2" icon={<CameraTwoTone />} title="Memorias">
              <Menu.Item key="5">Gabriel Anta</Menu.Item>
              <Menu.Item key="6">Douglas Cedeño</Menu.Item>
              <Menu.Item key="7">Raw Shoots</Menu.Item>
              <Menu.Item key="8">Geoff Photography</Menu.Item>
            </SubMenu>
            <SubMenu key="sub3" icon={<GiftTwoTone />} title="Decoraciones">
              <Menu.Item key="9">Floristería Costa Rica</Menu.Item>
              <Menu.Item key="10">Flores Gala</Menu.Item>
              <Menu.Item key="11">Juno Flowers</Menu.Item>
              <Menu.Item key="12">Nandallo</Menu.Item>
            </SubMenu>
          </Menu>
        </Sider>
        
        <Image
          width={600}
          src="https://thekingstonhome.com/wp-content/uploads/2020/01/forever-and-ever_v4-1024x232.png"
        />
        <Content style={{ padding: "0 24px", minHeight: 280 }}></Content>
      </Layout>
    </Content>

    <Footer style={{ textAlign: "center" }}>
      Created by Felipe-Maykol-Eduardo & Fernando ©2021{" "}
    </Footer>
  </Layout>
    )
}

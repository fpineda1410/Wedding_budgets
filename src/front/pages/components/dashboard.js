import React,{useContext,useEffect,useState} from "react";

import "antd/dist/antd.css";
import "../css/dashboard.css";
import { Layout, Menu, Image } from "antd";
import {
  GiftTwoTone,
  BankTwoTone,
  CameraTwoTone,
  ShoppingTwoTone,
  IdcardTwoTone,
  PhoneTwoTone,
  WalletTwoTone,
  DeleteFilled
} from "@ant-design/icons";

import { Statistic, Row, Col } from "antd";
import { LikeOutlined } from "@ant-design/icons";

const { SubMenu } = Menu;
const { Header, Content, Footer, Sider } = Layout;

import { Context } from "../../store/appContext.js";

import CardGenerator from "./card_generator_method/card_generator.js";
import Checkout_form from "./checkout_modal/modal.js"
import Info_form from "./checkout_modal/information_modal.js"

export const Dashboard = () => {
    const { store, actions } = useContext(Context);
    const [ show, isShowing ] = useState(false);
    const [card_data, setCardData]= useState('');
    const [showModal , setShowModal] = useState(false)
    const [showInfoModal , setInfoModal] = useState(false)
    
    useEffect(()=>{
        actions.information_sorting_generator_flowers();
        actions.information_sorting_generator_locations();
        actions.information_sorting_generator_photo();
        },[store.services_data,store.bearer_token])
    
if (store.bearer_token){
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
                    <Menu.Item key="1" onClick={()=>{
                        if (showModal){
                            setInfoModal(false);
                            setTimeout(()=>{setInfoModal(true);},200) 
                        }else{
                            setInfoModal(true);
                        }
                        }}>
                        <WalletTwoTone />
                        CheckOut
                    </Menu.Item>
                    <Menu.Item key="2"
                    onClick={()=>{
                        if (showInfoModal){
                            setShowModal(false);
                            setTimeout(()=>{setShowModal(true);},200) 
                        }else{
                            setShowModal(true);
                        }
                        }}>
                        <PhoneTwoTone />Contactenos
                    </Menu.Item>


                </Menu>
            </Header>
            <Content style={{ padding: "0 50px" }}>

                <Layout className="site-layout-background" style={{ padding: "24px 0" }}>
                    <Sider className="site-layout-background" width={200}>
                        <Menu
                            mode="inline"
                            style={{ height: "100%" }}
                        >
                            <SubMenu key="sub1" icon={<BankTwoTone />} title="Lugares">
                                <Menu.Item key="1" onClick={() => {
                                    isShowing(true);
                                    setCardData(store.herradura_data);
                                    
                                }}>Windham Herradura</Menu.Item>
                                <Menu.Item key="2" onClick={()=>{
                                    isShowing(true);
                                    setCardData(store.papagayo_data);
                                }}>Occidental Papagayo</Menu.Item>

                                <Menu.Item key="3" onClick={()=>{
                                    isShowing(true);
                                    setCardData(store.swiss_travel_data);
                                }}>Swiss Travel</Menu.Item>

                                <Menu.Item key="4" onClick={()=>{
                                    isShowing(true);
                                    setCardData(store.sheraton_data);
                                }}>Sheraton Escazu</Menu.Item>
                            </SubMenu>

                            <SubMenu key="sub2" icon={<CameraTwoTone />} title="Memorias">
                                <Menu.Item key="5" onClick={()=>{
                                    console.log(store.gabriel_anta_data);
                                    isShowing(true);
                                    setCardData(store.gabriel_anta_data);
                                }}
                                >Gabriel Anta</Menu.Item>

                                <Menu.Item key="6" onClick={()=>{
                                    console.log(store.douglas_cedeno_data);
                                    isShowing(true);
                                    setCardData(store.douglas_cedeno_data);
                                }}>Douglas Cedeño</Menu.Item>

                                <Menu.Item key="7"onClick={()=>{
                                    console.log(store.raw_shoots_data);
                                    isShowing(true);
                                    setCardData(store.raw_shoots_data);
                                }}>Raw Shoots</Menu.Item>

                                <Menu.Item key="8"onClick={()=>{
                                    console.log(store.geoff_photography_data);
                                    isShowing(true);
                                    setCardData(store.geoff_photography_data);
                                }}>Geoff Photography</Menu.Item>
                            </SubMenu>

                            <SubMenu key="sub3" icon={<GiftTwoTone />} title="Decoraciones">
                                <Menu.Item key="9" onClick={()=>{
                                    console.log(store.flores_cr_data);
                                    isShowing(true);
                                    setCardData(store.flores_cr_data);
                                }}
                                >Floristería Costa Rica</Menu.Item>

                                <Menu.Item key="10" onClick={()=>{
                                    console.log(store.flores_gala_data);
                                    isShowing(true);
                                    setCardData(store.flores_gala_data);
                                }}>Flores Gala</Menu.Item>

                                <Menu.Item key="11" onClick={()=>{
                                    console.log(store.flores_juno_data);
                                    isShowing(true);
                                    setCardData(store.flores_juno_data);
                                }}>Juno Flowers</Menu.Item>

                                <Menu.Item key="12" onClick={()=>{
                                    console.log(store.flores_nandallo_data);
                                    isShowing(true);
                                    setCardData(store.flores_nandallo_data);
                                }}>Nandallo</Menu.Item>

                            </SubMenu>
                             <SubMenu key="sub4" icon={<ShoppingTwoTone />} title="Mi canasta">

                                 {store.flower_indicator?//1,4,5
                                 <Menu.Item key="13" >
                                     <DeleteFilled
                                        key="delete"
                                        onClick={() => {
                                            actions.deleteItem({category:'Flowers', id: store.flower_indicator});
                                        }}
									/>{store.flower_provider}</Menu.Item>:''}
                                 {store.location_indicator?//1,4,5
                                 <Menu.Item key="14">
                                     <DeleteFilled
                                        key="delete"
                                        onClick={() => {
                                            actions.deleteItem({category:'Location', id: store.location_indicator});
                                        }}
									/>{store.location_provider}</Menu.Item>:''}
                                 {store.photo_indicator? //1,4,5
                                 <Menu.Item key="15">
                                     <DeleteFilled
                                        key="delete"
                                        onClick={() => {
                                            actions.deleteItem({category:'Photography', id: store.photo_indicator});
                                        }}
								/>{store.photo_provider}</Menu.Item>:''}

                             </SubMenu>
                        </Menu>
                    </Sider>

                    {show ?         
                    <CardGenerator list = {card_data}
                    /> 
                    :''}
                    {showModal?
                    <Info_form />
                    :''}
                    {showInfoModal?
                    <Checkout_form 
                     service_1_id={store.flower_indicator}
                     service_2_id={store.location_indicator}
                     service_3_id={store.photo_indicator}
                    />
                    :''}

                    <Content style={{ padding: "0 24px", minHeight: 280 }}></Content>
                </Layout>
            </Content>

            <Footer style={{ textAlign: "center" }}>
                Wedding Budgets. Todos los Derechos Reservados ©2021{" "}
            </Footer>
        </Layout>
    )
    }else{
        console.log(store.bearer_token)
        return (<div>404 Access Denied</div>)
    }
}

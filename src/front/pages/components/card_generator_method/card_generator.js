import React,{useContext} from "react";

import "antd/dist/antd.css";
import { Layout, Menu, Row, Col, Typography, Card, Avatar} from "antd";

const { Meta } = Card;

import {
	EllipsisOutlined,
	HeartFilled
} from "@ant-design/icons";

import { Link } from "react-router-dom";

import { Context } from "../../../store/appContext.js";

function CardGenerator ({ list,type })  {
    const {store, actions} =useContext(Context);
		return list.map((item, index) => (
			<Col className="gutter-row" span={4} style={{ margin: "5vh" }} key={index}>
				<Card
                    hoverable
					key={item.id}
					style={{ width: 250 }}
					cover={<img alt="example" src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png" />}
					actions={[
						<HeartFilled
							key={item.id}
							onClick={() =>
								{actions.update_local_budget_data({ category: item.category , id: item.id, name: item.provider })}
							}
						/>,
						<Link key={index} to={"/detail/1/" + index}>
							<EllipsisOutlined key="ellipsis" />
						</Link>
					]}>

					<Meta
						avatar={<Avatar src="https://www.policymed.com/wp-content/uploads/2013/04/6a00e5520572bb8834017c3875ac22970b.jpg" />}
						title="Proovedor"
						description=""
					/>

                    <p>{item.provider}</p>
                    <p><strong>Precio:</strong>${item.price}</p>
				</Card>
			</Col>
		));
    };
    
    export default CardGenerator;
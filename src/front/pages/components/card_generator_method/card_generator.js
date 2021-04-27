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
			<Col className="gutter-row" span={4} style={{ margin: "8vh" }} key={index}>
				<Card
                    hoverable
					key={item.id}
					style={{ width: 500 }}
					cover={<img alt="example" src={item.url} />}
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
						avatar={<Avatar src="https://images.vexels.com/media/users/3/137321/isolated/preview/72838e83cb97970f18dcd02d7965c0ed-heart-logo-couple-by-vexels.png" />}
						title="Proovedor"
						description=""
					/>

                    <p>{item.provider}</p>
                    <p><strong>Precio:</strong>${item.price}</p>
                    <p><strong>Precio aprox. colones:</strong>Colones {Math.round(parseInt(item.price)*store.USDvsCRC)}</p>
				</Card>
			</Col>
		));
    };
    
    export default CardGenerator;

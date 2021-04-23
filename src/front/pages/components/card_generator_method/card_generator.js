import "antd/dist/antd.css";
import { Layout, Menu, Row, Col, Typography, Card, Avatar } from "antd";

import {
	EllipsisOutlined,
	HeartFilled
} from "@ant-design/icons";
import { Link } from "react-router-dom";


const CardGeneratorPlanets = ({ list }) => {
		return list.map((item, index) => (
			<Col className="gutter-row" span={4} style={{ margin: "1vh" }} key={index}>
				<Card
					key={index}
					style={{ width: 250 }}
					cover={<img alt="example" src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png" />}
					actions={[
						<HeartFilled
							key={index}
							/*onClick={() =>
								actions.pushDataPlanets({ title: store.planet_data[index].name, id: index + 1 })
							}*/
						/>,
						<Link key={index} to={"/detail/1/" + index}>
							<EllipsisOutlined key="ellipsis" />
						</Link>
					]}>
					<Meta
						avatar={<Avatar src="https://www.policymed.com/wp-content/uploads/2013/04/6a00e5520572bb8834017c3875ac22970b.jpg" />}
						title="titulo de ejemplo"
						description="Planet"
					/>
				</Card>
			</Col>
		));
	};
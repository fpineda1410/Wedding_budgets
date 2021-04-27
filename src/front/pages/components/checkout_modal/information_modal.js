import React, { useContext, useState,useEffect } from 'react';
import { Modal, Button } from 'antd';


import { Context } from "../../../store/appContext.js";

function Info_form () {

  const [visible, setVisible] = useState(true);
  
  const { store, actions } = useContext(Context);
   
  return (
    <>
      <Modal
        title="Información de contacto:"
        centered
        visible={visible}
        onOk={() => setVisible(false)}
        onCancel={() => setVisible(false)}
        width={1000}
      >
        
        <p>Numero Telefonico<strong> 666</strong></p>
        
      </Modal>
    </>
  );
};

export default Info_form;
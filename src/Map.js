import GoogleMapReact from 'google-map-react';
import React from 'react';
import './index.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faMapMarkerAlt } from '@fortawesome/free-solid-svg-icons';

export default function Map(props) {
    const defaultProps = {
        center: {
          lat: -21.870333,
          lng: 120.101598
        },
        zoom: 8
      };
    
    // Check if googleMapApi prop is defined and not null
    // if (!props.googleMapApi) {
    //     return null;
    // }
    return (
        <div style={{ height: '100vh', width: '100%' }}>
            <GoogleMapReact 
                bootstrapURLKeys={{ key: props.googleMapApi }}
                defaultCenter={defaultProps.center}
                defaultZoom={defaultProps.zoom}>
                {props.marks.map((mark, index) => (
                <Marker key={index} lat={mark.latitude} lng={mark.longitude}>
                </Marker>))}
            </GoogleMapReact>
        </div>
    )
}

function Marker() {
    return (
      <div style={{ color: 'green', fontSize: '15px' }}>
        <FontAwesomeIcon icon={faMapMarkerAlt} />
      </div>
    );
  }


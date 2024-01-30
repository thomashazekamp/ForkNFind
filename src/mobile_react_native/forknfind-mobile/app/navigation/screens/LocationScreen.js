import React, { useState, useEffect } from 'react';
import { View, StyleSheet, StatusBar, Image, ActivityIndicator } from 'react-native';
import { Marker, Callout } from 'react-native-maps';
import MapView from "react-native-map-clustering";

import * as Location from 'expo-location';

import NearbyRestaurantsAPIRequest from '../requests/NearbyRestaurantsAPIRequest';
import RestaurantCardMap from '../components/RestaurantCardMap';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Functional Component LoginScreen
// navigation - used to link to other screens created
export default function LocationScreen({ navigation }) {

    // Use states to manage the information
    const [deviceLocation, setDeviceLocation] = useState(null);
    const [data, setData] = useState(null)

    // Reference: https://stackoverflow.com/questions/68955119/react-native-expo-location-returns-location-service-unavailable-during-initial-u
    // Response by user Dharman, Aug 27th 2021
    // This code was adapted from a solution found online on stack overflow
    useEffect(() => {
        (async () => {
        const { status } = await Location.requestForegroundPermissionsAsync();
        if (status === 'granted') {
            const locationData = await Location.getCurrentPositionAsync({});
            setDeviceLocation(locationData);
            saveLocationData(locationData)

            NearbyRestaurantsAPIRequest(setData, locationData);

        }
        })();
    }, []);

    const saveLocationData = async (locationData) => {
        try {
            await AsyncStorage.setItem(
                "locationDataLongitude", String(locationData['coords']['longitude'])
            )
            await AsyncStorage.setItem(
                "locationDataLatitude", String(locationData['coords']['latitude'])
            )
        } catch (error) {
            console.log(error)
        }
    }

    return (
        // Map view code using React library
        <View style={styles.container}>
            <StatusBar barStyle="light-content" />
                {data !== null ? 
                <MapView
                    style={styles.map}
                    initialRegion={{
                        latitude: deviceLocation["coords"]["latitude"],
                        longitude: deviceLocation["coords"]["longitude"],
                        latitudeDelta: 0.045,
                        longitudeDelta: 0.02,
                }}
                    showsPointsOfInterest={false}
                >
                    {/* Mark user location */}
                    <Marker
                        coordinate={{
                        latitude: deviceLocation["coords"]["latitude"],
                        longitude: deviceLocation["coords"]["longitude"],
                        }}
                        title="Your Location"
                        description="You are here"
                    />
                    {/* Mark the restaurant locations by looping through data */}
                    {Object.keys(data).map(key => ( 
                    <Marker key={key} coordinate={{ latitude: data[key]["location"][1], longitude: data[key]["location"][0]}} >
                        <Image
                        source={require('../../../image/custom_marker.png')}
                        style={{width: 33, height:48, marginBottom: 40}}
                        />
                        <Callout tooltip={true} >
                            <RestaurantCardMap restaurantData={data[key]} />
                        </Callout>
                    </Marker> ))}
                </MapView>
                :
                <View style={{
                    flex: 1, 
                    alignItems: 'center',
                    justifyContent: 'center', 
                }}> 
                    <ActivityIndicator size="large" color="#1C58F2" />
                </View>
                }
        </View>
    );
}

/* <Image source={require('../../../image/custom_marker.png')} style={{ width: 50, height: 50 }}/> */
const styles = StyleSheet.create({
    // Container takig the whole screen
    container: {
        ...StyleSheet.absoluteFillObject,
        flex: 1,
        justifyContent: 'flex-end',
        alignItems: 'center',
    },
    // map taking up all the space
    map: {
        ...StyleSheet.absoluteFillObject,
    }
});
import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import { FontAwesome } from '@expo/vector-icons';
import IndividualRestaurantModal from './IndividualRestaurantModal';

// Functional Component RestaurantCard
// restaurantData - data for an individual restaurant
const RestaurantCard = ( {restaurantData}) => {

    // Use state for if the modal is visible or not
    const [modalVisible, setModalVisible] = useState(false);

    // Restaurant data
    const {
        id,
        name,
        type,
        price_level,
        average_rating,
        distance_from_user,
        open_or_close,
    } = restaurantData;

    // Toggling the modal
    const toggleModal = () => {
        setModalVisible(!modalVisible);
    }

    return ( 
        /* Having the whole card selectable to pull up individual restaurant information */
        <TouchableOpacity style={styles.container} onPress={() => toggleModal()}>
            <View style={styles.containerNameStatus}>
                <Text style={styles.restaurantName}>{name}</Text>
                <View style={styles.containerRestaurantStatus}>
                    <FontAwesome name="check-circle"  size={14} color={"white"} style={{marginRight: "5%"}}/>
                    <Text style={styles.restaurantStatus}>{open_or_close}</Text>
                </View>
            </View>
            <View style={styles.containerStarRatingPrice}>
            <View style={styles.columnStar}>
                <AntDesign name="star" size={22} color="#DBFF00" style={{position: 'absolute', right: '5%',paddingTop: "14%"}} />
                <AntDesign name="staro" size={22} color="#000000" style={{position: 'absolute', right: '5%',paddingTop: "14%"}} />
            </View>
            <View style={styles.columnRating}>
                    <Text style={styles.restaurantAverageRating}>{average_rating}/5 (2)</Text>
            </View>
            <View style={styles.columnPrice}>
                <Text style={styles.restaurantPriceLevel}>{price_level}</Text>
            </View>
            <View style={styles.columnCard}>
                <AntDesign name="creditcard" size={20} color="black" style={{position: 'absolute', left: '5%',paddingTop: "30%"}}/>
            </View>
        </View>
        <View style={styles.containerTypeDistance}>
                <View style={styles.typeBox}>
                <Text style={styles.typeText}>{type}</Text>
            </View>
            <Text style={styles.distanceText}>{distance_from_user.toFixed(1)} Km</Text>
        </View>
        {/* To get modal to appear */}
        {modalVisible && (
          <IndividualRestaurantModal
              visible={modalVisible}
              onClose={() => setModalVisible(false)}
              id={id}
              distance={distance_from_user.toFixed(1)}
          />
        )}
    </TouchableOpacity>
    );
}

const styles = StyleSheet.create({
    // Container styling
    container: {
        width: '90%',
        height: 120,
        left: '5%',
        right: '5%',
        marginTop: '2.5%',
        marginBottom: '2.5%',
        backgroundColor: 'white',
        borderRadius: 20
    },
    // Distance between name and open/close bar
    containerNameStatus: {
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    // Name styling
    restaurantName: {
        paddingTop: '5%',
        paddingLeft: '7.5%',
        fontSize: 18,
        fontWeight: 'bold',
        color: '#181A1F'
    },
    // open close styling
    containerRestaurantStatus: {
        flexDirection: 'row',
        backgroundColor: '#07864B',
        position: 'absolute',
        top: 20,
        right: 0,
        width: 80,
        height: 20,

        borderTopLeftRadius: 7,
        borderBottomLeftRadius: 7,

        justifyContent: 'center',
        alignItems: 'center',
    },
    // Colour for the status
    restaurantStatus: {
        color: '#FFFFFF',
        fontWeight: 'bold',
    },
    // Average rating styling
    restaurantAverageRating: {
        paddingTop: '6%',
        paddingLeft: '0%',
        fontWeight: '600',
        fontSize: 15,
    },
    // Restaurant price level styling
    restaurantPriceLevel: {
        paddingTop: '10%',
        paddingRight: '0%',
        fontWeight: '600',
        fontSize: 17,
        position: 'absolute', 
        right: '5%',
    },
    // Container styling
    containerStarRatingPrice: {
        flexDirection: 'row',
    },
    columnStar: {
        width: '14.2%',
    },
    columnRating: {
        width: '45%'
    },
    columnPrice: {
        width: '31%'
    },
    columnCard: {
        width: '10%'
    },
    containerTypeDistance: {
        flexDirection: 'row',
    },
    // Type of restaurant styling
    typeBox: {
        marginTop: '4.2%',
        marginLeft: '7.5%',
        paddingLeft: 7,
        paddingRight: 7,
        paddingBottom: 2,
        paddingTop: 1,
        borderRadius: 50,
        backgroundColor: '#F5F7FC',
    },
    // Text inside the container for type
    typeText: {
        fontSize: 13,
        color: '#181A1F',
        fontWeight: '500',
    },
    // Styling for the text that contains the distance
    distanceText: {
        fontSize: 17,
        position: 'absolute',
        marginTop: '3.9%',
        right: 20,
        fontWeight: '500',
    },
});

export default RestaurantCard;
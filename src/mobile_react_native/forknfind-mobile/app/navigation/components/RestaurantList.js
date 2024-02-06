import React, { memo } from 'react';
import RestaurantCard from './RestaurantCard';
import { View, } from 'react-native';

// Function RestaurantList
// data - Restaurant data containing all restaurants
const RestaurantList = memo(({ data }) => (
    // Wrap component in memo to save the data such that it will only reload on data changing
    <View>
        {/* Looping through results from search */}
        {data.map(item => (
            <RestaurantCard key={item.id} restaurantData={item} />
        ))}
    </View>
));

export default RestaurantList;
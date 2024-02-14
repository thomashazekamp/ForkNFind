import React, { memo } from 'react';
import { View, } from 'react-native';
import ReviewCardRestaurant from './ReviewCardRestaurant';

// Function ReviewRestaurantList
// data - Review data containing all reviews
const ReviewRestaurantList = memo(({ data }) => (
    // Wrap component in memo to save the data such that it will only reload on data changing
    <View>
        {/* Looping through reviews */}
        {data.map(item => (
            <ReviewCardRestaurant key={item.id} data={item} />
        ))}
    </View>
));

export default ReviewRestaurantList;
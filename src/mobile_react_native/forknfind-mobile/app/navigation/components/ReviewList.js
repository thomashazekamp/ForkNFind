import React, { memo } from 'react';
import { View, } from 'react-native';
import ReviewCard from './ReviewCard';

// Function ReviewCard
// data - Review data containing all reviews
const ReviewList = memo(({ data, setReload }) => (
    // Wrap component in memo to save the data such that it will only reload on data changing
    <View>
        {/* Looping through reviews */}
        {data.map(item => (
            <ReviewCard key={item.id} data={item} setReload={setReload} />
        ))}
    </View>
));

export default ReviewList;
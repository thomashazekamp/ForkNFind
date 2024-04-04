import React from 'react';
import { render } from '@testing-library/react-native';
import CreateReviewScreen from '../CreateReviewScreen';

describe('CreateReviewScreen', () => {
    // mock the restaurant data, needed for the screen
    const mockRestaurantData = { name: 'Test Restaurant' };
    
    it('Should have a Submit', () => {
        // render the review screen with a given restaurant name
        const { getByText } = render(<CreateReviewScreen restaurantData={mockRestaurantData} />);
        // check that the screen has rendered
        expect(getByText('Submit')).toBeTruthy();
    });
    it('Should have a adding review', () => {
        // render the review screen with a given restaurant name
        const { getByText } = render(<CreateReviewScreen restaurantData={mockRestaurantData} />);
        // check that the screen has rendered
        expect(getByText('Add detailed Review')).toBeTruthy();
    });
    it('Should have your rating', () => {
        // render the review screen with a given restaurant name
        const { getByText } = render(<CreateReviewScreen restaurantData={mockRestaurantData} />);
        // check that the screen has rendered
        expect(getByText('Your Rating')).toBeTruthy();
    });
});
import React from 'react';
import { render } from '@testing-library/react-native';
import CreateReviewScreen from '../CreateReviewScreen';

describe('CreateReviewScreen', () => {
  it('Should render', () => {
    // mock the restaurant data, needed for the screen
    const mockRestaurantData = { name: 'Test Restaurant' };
    // render the review screen with a given restaurant name
    const { getByText } = render(<CreateReviewScreen restaurantData={mockRestaurantData} />);
    // check that the screen has rendered
    expect(getByText('Submit')).toBeTruthy();
  });
});
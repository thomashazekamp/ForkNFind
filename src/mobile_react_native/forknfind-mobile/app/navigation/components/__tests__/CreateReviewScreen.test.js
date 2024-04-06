import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import CreateReviewScreen from '../CreateReviewScreen';
import { create } from 'react-test-renderer';

describe('CreateReviewScreen', () => {
    // mock the restaurant data, needed for the screen
    const mockRestaurantData = { name: 'Test Restaurant' };

    it('Should have 3 children', () => {
        // check that the screen has 3 children
        const tree = create(<CreateReviewScreen restaurantData={mockRestaurantData} />).toJSON();
        expect(tree.children.length).toBe(3);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<CreateReviewScreen restaurantData={mockRestaurantData} />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have a Submit', async () => {
        // render the review screen with a given restaurant name
        const { getByText } = render(<CreateReviewScreen restaurantData={mockRestaurantData} />);
        // wait for the network request to complete
        await waitFor(() => getByText('Submit'), {timeout: 10000});
        // check that the screen has rendered
        expect(getByText('Submit')).toBeTruthy();
    });
    it('Should have a adding review', async () => {
        // render the review screen with a given restaurant name
        const { getByText } = render(<CreateReviewScreen restaurantData={mockRestaurantData} />);
        // wait for the network request to complete
        await waitFor(() => getByText('Add detailed Review'), {timeout: 10000});
        // check that the screen has rendered
        expect(getByText('Add detailed Review')).toBeTruthy();
    });
    it('Should have your rating', async () => {
        // render the review screen with a given restaurant name
        const { getByText } = render(<CreateReviewScreen restaurantData={mockRestaurantData} />);
        // wait for the network request to complete
        await waitFor(() => getByText('Your Rating'), {timeout: 10000});
        // check that the screen has rendered
        expect(getByText('Your Rating')).toBeTruthy();
    });
});
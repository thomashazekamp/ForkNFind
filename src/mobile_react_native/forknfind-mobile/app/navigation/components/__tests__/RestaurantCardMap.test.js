import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import RestaurantCardMap from '../RestaurantCardMap';
import { create } from 'react-test-renderer';

describe('RestaurantCardMap', () => {
    // mock the review data, needed for the screen
    const mockData = {
        id: '1',
        name: 'Test Restaurant',
        type: 'Italian',
        price_level: '3',
        average_rating: 4.3,
        distance_from_user: 2,
        open_or_close: 'Open',
        review_number: 1,
      };

    it('Should have 3 children', () => {
        // check that the screen has 3 children
        const tree = create(<RestaurantCardMap restaurantData={mockData} />).toJSON();
        expect(tree.children.length).toBe(3);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<RestaurantCardMap restaurantData={mockData} />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have open or close', () => {
        // render the review screen with a given data
        const { getByText } = render(<RestaurantCardMap restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText(mockData.open_or_close)).toBeTruthy();
    });

    it('Should have rating', () => {
        // render the review screen with a given data
        const { getByText } = render(<RestaurantCardMap restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText(mockData.average_rating + '/5 (' + mockData.review_number + ')')).toBeTruthy();
    });

    it('Should have price level', () => {
        // render the review screen with a given data
        const { getByText } = render(<RestaurantCardMap restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText(mockData.price_level)).toBeTruthy();
    });

    it('Should have name', () => {
        // render the review screen with a given data
        const { getByText } = render(<RestaurantCardMap restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText(mockData.name)).toBeTruthy();
    });

    it('Should have type', () => {
        // render the review screen with a given data
        const { getByText } = render(<RestaurantCardMap restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText(mockData.type)).toBeTruthy();
    });
});
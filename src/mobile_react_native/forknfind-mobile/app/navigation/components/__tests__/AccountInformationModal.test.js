import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import AccountInformationModal from '../AccountinformationModal';
import { create } from 'react-test-renderer';

describe('AccountInformationModal', () => {
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
      global.access_global = 'token_test'

    it('Should have 2 children', () => {
        // check that the screen has 3 children
        const tree = create(<AccountInformationModal restaurantData={mockData} />).toJSON();
        expect(tree.children.length).toBe(2);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<AccountInformationModal restaurantData={mockData} />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have First name', () => {
        // render the review screen with a given data
        const { getByText } = render(<AccountInformationModal restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('First Name')).toBeTruthy();
    });

    it('Should have last name', () => {
        // render the review screen with a given data
        const { getByText } = render(<AccountInformationModal restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('Last Name')).toBeTruthy();
    });

    it('Should have username', () => {
        // render the review screen with a given data
        const { getByText } = render(<AccountInformationModal restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('Username')).toBeTruthy();
    });

    it('Should have email', () => {
        // render the review screen with a given data
        const { getByText } = render(<AccountInformationModal restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('Email')).toBeTruthy();
    });

    it('Should have Close', () => {
        // render the review screen with a given data
        const { getByText } = render(<AccountInformationModal restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('Close')).toBeTruthy();
    });
});
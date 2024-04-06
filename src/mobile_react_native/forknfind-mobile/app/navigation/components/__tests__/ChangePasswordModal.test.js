import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import ChangePasswordModal from '../ChangePasswordModal';
import { create } from 'react-test-renderer';

describe('ChangePasswordModal', () => {
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

    it('Should have 1 children', () => {
        // check that the screen has 3 children
        const tree = create(<ChangePasswordModal restaurantData={mockData} />).toJSON();
        expect(tree.children.length).toBe(1);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<ChangePasswordModal restaurantData={mockData} />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have Current password', () => {
        // render the review screen with a given data
        const { getByText } = render(<ChangePasswordModal restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('Current Password')).toBeTruthy();
    });

    it('Should have New password', () => {
        // render the review screen with a given data
        const { getByText } = render(<ChangePasswordModal restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('New Password')).toBeTruthy();
    });

    it('Should have back', () => {
        // render the review screen with a given data
        const { getByText } = render(<ChangePasswordModal restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('Back')).toBeTruthy();
    });
});
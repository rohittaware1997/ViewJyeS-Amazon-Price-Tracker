// Import the necessary packages for testing
import { describe, expect, it } from '@jest/globals';
import { installQuasarPlugin } from '@quasar/quasar-app-extension-testing-unit-jest';
import { mount } from '@vue/test-utils';
import SignIn from 'layouts/SignIn.vue';

installQuasarPlugin();

describe('SignIn', () => {
  // Test for successful login
  it('logs in successfully', async () => {
    // Create a mock router and Vuex store
    const router = {
      push: jest.fn(),
    };
    const store = {
      dispatch: jest.fn(),
    };

    // Mount the component and provide necessary props and mocks
    const wrapper = mount(SignIn, {
      global: {
        plugins: [store],
        mocks: {
          $router: router,
        },
      },
    });

    // Set the input values
    wrapper.find('input[type="text"]').setValue('testuser@test.com');
    wrapper.find('input[type="password"]').setValue('testpassword');

    // Mock the signInWithEmailAndPassword function
    const signInWithEmailAndPassword = jest.fn();
    wrapper.vm.$options.methods.signInWithEmailAndPassword = signInWithEmailAndPassword;

    // Trigger the click event of the login button
    await wrapper.find('#login_button').trigger('click');

    // Check if the signInWithEmailAndPassword function was called
    expect(signInWithEmailAndPassword).toHaveBeenCalled();

    // Check if the router was redirected to the correct page
    expect(router.push).toHaveBeenCalledWith('/search');

    // Check if the Vuex store was updated with the correct values
    expect(store.dispatch).toHaveBeenCalledWith('amazon/updateEmailId', 'testuser@test.com');
    expect(store.dispatch).toHaveBeenCalledWith('amazon/updateFullName', 'Test User');
    // expect(store.dispatch).toHaveBeenCalledWith('amazon/updateCardDetail', {...});
  });

  // Test for unsuccessful login with invalid email
  it('displays error message for invalid email', async () => {
    const wrapper = mount(SignIn);

    wrapper.find('input[type="text"]').setValue('invalidemail');
    wrapper.find('input[type="password"]').setValue('testpassword');

    const signInWithEmailAndPassword = jest.fn(() => {
      throw { code: 'auth/invalid-email' };
    });
    wrapper.vm.$options.methods.signInWithEmailAndPassword = signInWithEmailAndPassword;

    await wrapper.find('#login_button').trigger('click');

    expect(signInWithEmailAndPassword).toHaveBeenCalled();
    expect(wrapper.find('p').text()).toBe('Invalid email');
  });

  // Test for unsuccessful login with incorrect password
  it('displays error message for incorrect password', async () => {
    const wrapper = mount(SignIn);

    wrapper.find('input[type="text"]').setValue('testuser@test.com');
    wrapper.find('input[type="password"]').setValue('incorrectpassword');

    const signInWithEmailAndPassword = jest.fn(() => {
      throw { code: 'auth/wrong-password' };
    });
    wrapper.vm.$options.methods.signInWithEmailAndPassword = signInWithEmailAndPassword;

    await wrapper.find('#login_button').trigger('click');

    expect(signInWithEmailAndPassword).toHaveBeenCalled();
    expect(wrapper.find('p').text()).toBe(' Incorrect password');
  });

  // Test for unsuccessful login with unknown error
  it('displays error message for unknown error', async () => {
    const wrapper = mount(SignIn);

    wrapper.find('input[type="text"]').setValue('testuser@test.com');
    wrapper.find('input[type="password"]').setValue('testpassword');

    const signInWithEmailAndPassword = jest.fn(() => {
      throw { code: 'auth/unknown-error' };
    });
    wrapper.vm.$options.methods.signInWithEmailAndPassword = signInWithEmailAndPassword;

    await wrapper.find('#login_button').trigger('click');

    expect(signInWithEmailAndPassword).toHaveBeenCalled();
    expect(wrapper.find('p').text()).toBe('Email or password was incorrect');
  });
});

import { describe, expect, it } from '@jest/globals';
import { installQuasarPlugin } from '@quasar/quasar-app-extension-testing-unit-jest';
import {mount, shallowMount} from '@vue/test-utils';
import AppDrawer from 'components/AppDrawer/AppDrawer.vue';

installQuasarPlugin();

describe("AppDrawer", () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(AppDrawer);
  });

  afterEach(() => {
    wrapper.unmount();
  });

  it("renders the component", () => {
    expect(wrapper.exists()).toBe(true);
  });

  it("updates the isLoggedIn value when the user is authenticated", () => {
    wrapper.vm.$options.setup[0](); // call the onMounted hook
    expect(wrapper.vm.isLoggedIn).toBe(false); // initially not authenticated
    wrapper.vm.$options.setup[0].toReturn.onAuthStateChanged({
      uid: "abc123",
      email: "test@example.com",
    }); // simulate authentication
    expect(wrapper.vm.isLoggedIn).toBe(true); // should be authenticated now
  });
  it("updates the isLoggedIn value when the user signs out", async () => {
    wrapper.vm.$options.setup[0](); // call the onMounted hook
    expect(wrapper.vm.isLoggedIn).toBe(false); // initially not authenticated
    wrapper.vm.$options.setup[0].toReturn.onAuthStateChanged({
      uid: "abc123",
      email: "test@example.com",
    }); // simulate authentication
    expect(wrapper.vm.isLoggedIn).toBe(true); // should be authenticated now
    await wrapper.vm.handleSignOut(); // sign out
    expect(wrapper.vm.isLoggedIn).toBe(false); // should not be authenticated now
  });

  it("renders the appropriate navigation links based on the isLoggedIn value", async () => {
    expect(wrapper.findAll("a")).toHaveLength(2); // initially shows only Home and Register links
    expect(wrapper.find('a[href="/search"]').exists()).toBe(false); // should not show Track Link link
    wrapper.vm.$options.setup[0].toReturn.isLoggedIn.value = true; // set the isLoggedIn value to true
    await wrapper.vm.$nextTick(); // wait for reactivity
    expect(wrapper.findAll("a")).toHaveLength(4); // should now show all links except the Register link
    expect(wrapper.find('a[href="/search"]').exists()).toBe(true);
  });

});


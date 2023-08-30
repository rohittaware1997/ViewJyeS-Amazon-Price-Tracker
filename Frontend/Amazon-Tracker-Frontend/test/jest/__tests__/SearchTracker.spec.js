import { shallowMount } from '@vue/test-utils'
import SearchTracker from 'layouts/SearchTracker.vue'

describe('SearchTracker.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(SearchTracker);
  });

  afterEach(() => {
    wrapper.unmount();
  });

  it('renders the Amazon Link label', () => {
    expect(wrapper.find('.search-row-item-1').text()).toMatch('Amazon Link:');
  });

  it('updates text when input value changes', async () => {
    const input = wrapper.find('input');
    await input.setValue('https://www.amazon.com/dp/B08SBK64QH');
    expect(wrapper.vm.text).toBe('https://www.amazon.com/dp/B08SBK64QH');
  });

  it('sets priceDecrease to false when its toggle is clicked', async () => {
    const toggle1 = wrapper.find('.q-toggle:first-of-type');
    await toggle1.trigger('click');
    expect(wrapper.vm.priceDecrease).toBe(false);
  });

  it('sets everyHour to true when its toggle is clicked', async () => {
    const toggle2 = wrapper.find('.q-toggle:last-of-type');
    await toggle2.trigger('click');
    expect(wrapper.vm.everyHour).toBe(true);
  });

  it('displays an alert when track button is clicked and input is empty', async () => {
    window.alert = jest.fn();
    const trackBtn = wrapper.find('.q-btn');
    await trackBtn.trigger('click');
    expect(window.alert).toHaveBeenCalledWith('Enter a link');
  });

  // Mocking the API request
  const mockAxios = {
    put: jest.fn(() => Promise.resolve({ data: 'success' }))
  };

  it('calls setTracker and updates store when track button is clicked with valid input', async () => {
    const spyStore = jest.spyOn(wrapper.vm.$store, 'dispatch');
    wrapper.vm.text = 'https://www.amazon.com/dp/B08SBK64QH';
    wrapper.vm.priceDecrease = false;
    wrapper.vm.everyHour = true;
    wrapper.vm.setTracker = mockAxios.put;
    const trackBtn = wrapper.find('.q-btn');
    await trackBtn.trigger('click');
    expect(mockAxios.put).toHaveBeenCalledWith('http://127.0.0.1:5000/track', {
      link: 'https://www.amazon.com/dp/B08SBK64QH',
      toggleValue: 1,
      email: expect.any(String)
    });
    expect(spyStore).toHaveBeenCalledWith('amazon/updateCardDetail', 'success');
    expect(wrapper.vm.$router.currentRoute.value.path).toBe('/account');
  });

  it('displays an alert when setTracker function throws an error', async () => {
    window.alert = jest.fn();
    wrapper.vm.setTracker = jest.fn(() => Promise.reject('Error message'));
    const trackBtn = wrapper.find('.q-btn');
    await trackBtn.trigger('click');
    expect(window.alert).toHaveBeenCalledWith('Error message');
    expect(wrapper.vm.text).toBe('');
  });
});

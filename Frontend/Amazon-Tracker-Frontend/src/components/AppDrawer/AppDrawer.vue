<template>
  <q-layout view="lHh Lpr lff" class="rounded-borders">
    <q-header elevated class="bg-cyan-8">
      <q-toolbar>
        <q-toolbar-title class="text-center">Amazon Price Tracker</q-toolbar-title>
        <q-btn flat @click="drawer = !drawer" round dense icon="menu" />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="drawer"
      show-if-above
      :width="200"
      :breakpoint="400"
    >
      <q-scroll-area style="height: calc(100% - 150px); margin-top: 150px; border-right: 1px solid #ddd">
        <q-list padding>
          <q-item to="/search" clickable v-ripple v-if="isLoggedIn">
            <q-item-section avatar>
              <q-icon name="search" />
            </q-item-section>

            <q-item-section>
              Track Link
            </q-item-section>
          </q-item>

          <q-item to="/register"  clickable v-ripple v-if="!isLoggedIn">
            <q-item-section avatar>
              <q-icon name="how_to_reg" />
            </q-item-section>

            <q-item-section>
              Register
            </q-item-section>
          </q-item>

          <q-item to="/"  clickable v-ripple v-if="!isLoggedIn">
            <q-item-section avatar>
              <q-icon name="login" />
            </q-item-section>

            <q-item-section>
              Login
            </q-item-section>
          </q-item>

          <q-item to="/account" clickable v-ripple v-if="isLoggedIn">
            <q-item-section avatar>
              <q-icon name="account_circle" />
            </q-item-section>

            <q-item-section>
              Account
            </q-item-section>
          </q-item>

          <q-item clickable v-ripple v-if="isLoggedIn" @click="handleSignOut">
            <q-item-section avatar>
              <q-icon name="logout" />
            </q-item-section>

            <q-item-section>
              Sign Out
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>

      <q-img class="absolute-top" src="https://cdn.quasar.dev/img/material.png" style="height: 150px">
        <div class="absolute-bottom bg-transparent">
          <q-avatar size="86px" class="q-mb-sm" style="margin: auto; padding-left: 30px">
            <img src="~assets/user_icon.png">
          </q-avatar>
          <div class="text-weight-bold" style="text-align: center">{{ getFullName }}</div>
        </div>
      </q-img>
    </q-drawer>
    <q-page-container>
      <q-page padding>
        <router-view />
      </q-page>
    </q-page-container>
  </q-layout>
</template>


<script type="text/javascript" src="./AppDrawer.js"></script>
<style scoped lang="scss" src="./AppDrawer.scss"></style>

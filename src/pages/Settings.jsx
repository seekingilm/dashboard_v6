import React, { useState } from 'react';
import {
  Box,
  Paper,
  Typography,
  Grid,
  Switch,
  FormControlLabel,
  Divider,
  TextField,
  Button,
  Card,
  CardContent,
  Select,
  MenuItem,
  InputLabel,
  FormControl,
  Alert,
  Tabs,
  Tab,
  IconButton,
  Tooltip,
  Stack,
} from '@mui/material';
import {
  Brightness4 as DarkModeIcon,
  Notifications as NotificationsIcon,
  Security as SecurityIcon,
  Language as LanguageIcon,
  Save as SaveIcon,
  Info as InfoIcon,
  Email as EmailIcon,
  Phone as PhoneIcon,
  LocationOn as LocationIcon,
} from '@mui/icons-material';

const Settings = () => {
  const [activeTab, setActiveTab] = useState(0);
  const [showSuccess, setShowSuccess] = useState(false);
  const [settings, setSettings] = useState({
    // Appearance
    darkMode: false,
    language: 'en',
    fontSize: 'medium',
    // Notifications
    emailNotifications: true,
    pushNotifications: true,
    marketingEmails: false,
    // Security
    twoFactorAuth: false,
    sessionTimeout: '30',
    // Profile
    name: 'John Doe',
    email: 'john@example.com',
    phone: '+1 (555) 123-4567',
    location: 'San Francisco, CA',
    // System
    autoUpdate: true,
    analytics: true,
    backup: 'daily',
  });

  const handleChange = (event) => {
    const { name, value, checked } = event.target;
    setSettings((prev) => ({
      ...prev,
      [name]: event.target.type === 'checkbox' ? checked : value,
    }));
  };

  const handleSave = () => {
    setShowSuccess(true);
    setTimeout(() => setShowSuccess(false), 3000);
  };

  const handleTabChange = (event, newValue) => {
    setActiveTab(newValue);
  };

  const TabPanel = ({ children, value, index }) => (
    <Box role="tabpanel" hidden={value !== index} sx={{ py: 3 }}>
      {value === index && children}
    </Box>
  );

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Settings
      </Typography>

      {showSuccess && (
        <Alert severity="success" sx={{ mb: 2 }}>
          Settings saved successfully!
        </Alert>
      )}

      <Paper sx={{ mt: 3 }}>
        <Tabs
          value={activeTab}
          onChange={handleTabChange}
          variant="scrollable"
          scrollButtons="auto"
          sx={{ borderBottom: 1, borderColor: 'divider' }}
        >
          <Tab icon={<DarkModeIcon />} label="Appearance" />
          <Tab icon={<NotificationsIcon />} label="Notifications" />
          <Tab icon={<SecurityIcon />} label="Security" />
          <Tab icon={<EmailIcon />} label="Profile" />
          <Tab icon={<LanguageIcon />} label="System" />
        </Tabs>

        {/* Appearance Settings */}
        <TabPanel value={activeTab} index={0}>
          <Grid container spacing={3}>
            <Grid item xs={12} md={6}>
              <Card>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    Theme Settings
                  </Typography>
                  <Stack spacing={3}>
                    <FormControlLabel
                      control={
                        <Switch
                          checked={settings.darkMode}
                          onChange={handleChange}
                          name="darkMode"
                        />
                      }
                      label="Dark Mode"
                    />
                    <FormControl fullWidth>
                      <InputLabel>Language</InputLabel>
                      <Select
                        value={settings.language}
                        label="Language"
                        name="language"
                        onChange={handleChange}
                      >
                        <MenuItem value="en">English</MenuItem>
                        <MenuItem value="es">Spanish</MenuItem>
                        <MenuItem value="fr">French</MenuItem>
                        <MenuItem value="de">German</MenuItem>
                      </Select>
                    </FormControl>
                    <FormControl fullWidth>
                      <InputLabel>Font Size</InputLabel>
                      <Select
                        value={settings.fontSize}
                        label="Font Size"
                        name="fontSize"
                        onChange={handleChange}
                      >
                        <MenuItem value="small">Small</MenuItem>
                        <MenuItem value="medium">Medium</MenuItem>
                        <MenuItem value="large">Large</MenuItem>
                      </Select>
                    </FormControl>
                  </Stack>
                </CardContent>
              </Card>
            </Grid>
          </Grid>
        </TabPanel>

        {/* Notification Settings */}
        <TabPanel value={activeTab} index={1}>
          <Grid container spacing={3}>
            <Grid item xs={12} md={6}>
              <Card>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    Notification Preferences
                  </Typography>
                  <Stack spacing={2}>
                    <FormControlLabel
                      control={
                        <Switch
                          checked={settings.emailNotifications}
                          onChange={handleChange}
                          name="emailNotifications"
                        />
                      }
                      label="Email Notifications"
                    />
                    <FormControlLabel
                      control={
                        <Switch
                          checked={settings.pushNotifications}
                          onChange={handleChange}
                          name="pushNotifications"
                        />
                      }
                      label="Push Notifications"
                    />
                    <FormControlLabel
                      control={
                        <Switch
                          checked={settings.marketingEmails}
                          onChange={handleChange}
                          name="marketingEmails"
                        />
                      }
                      label="Marketing Emails"
                    />
                  </Stack>
                </CardContent>
              </Card>
            </Grid>
          </Grid>
        </TabPanel>

        {/* Security Settings */}
        <TabPanel value={activeTab} index={2}>
          <Grid container spacing={3}>
            <Grid item xs={12} md={6}>
              <Card>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    Security Settings
                  </Typography>
                  <Stack spacing={3}>
                    <FormControlLabel
                      control={
                        <Switch
                          checked={settings.twoFactorAuth}
                          onChange={handleChange}
                          name="twoFactorAuth"
                        />
                      }
                      label="Two-Factor Authentication"
                    />
                    <FormControl fullWidth>
                      <InputLabel>Session Timeout</InputLabel>
                      <Select
                        value={settings.sessionTimeout}
                        label="Session Timeout"
                        name="sessionTimeout"
                        onChange={handleChange}
                      >
                        <MenuItem value="15">15 minutes</MenuItem>
                        <MenuItem value="30">30 minutes</MenuItem>
                        <MenuItem value="60">1 hour</MenuItem>
                        <MenuItem value="120">2 hours</MenuItem>
                      </Select>
                    </FormControl>
                  </Stack>
                </CardContent>
              </Card>
            </Grid>
          </Grid>
        </TabPanel>

        {/* Profile Settings */}
        <TabPanel value={activeTab} index={3}>
          <Grid container spacing={3}>
            <Grid item xs={12} md={6}>
              <Card>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    Profile Information
                  </Typography>
                  <Stack spacing={3}>
                    <TextField
                      fullWidth
                      label="Name"
                      name="name"
                      value={settings.name}
                      onChange={handleChange}
                    />
                    <TextField
                      fullWidth
                      label="Email"
                      name="email"
                      value={settings.email}
                      onChange={handleChange}
                      type="email"
                    />
                    <TextField
                      fullWidth
                      label="Phone"
                      name="phone"
                      value={settings.phone}
                      onChange={handleChange}
                    />
                    <TextField
                      fullWidth
                      label="Location"
                      name="location"
                      value={settings.location}
                      onChange={handleChange}
                    />
                  </Stack>
                </CardContent>
              </Card>
            </Grid>
          </Grid>
        </TabPanel>

        {/* System Settings */}
        <TabPanel value={activeTab} index={4}>
          <Grid container spacing={3}>
            <Grid item xs={12} md={6}>
              <Card>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    System Preferences
                  </Typography>
                  <Stack spacing={3}>
                    <FormControlLabel
                      control={
                        <Switch
                          checked={settings.autoUpdate}
                          onChange={handleChange}
                          name="autoUpdate"
                        />
                      }
                      label="Automatic Updates"
                    />
                    <FormControlLabel
                      control={
                        <Switch
                          checked={settings.analytics}
                          onChange={handleChange}
                          name="analytics"
                        />
                      }
                      label="Usage Analytics"
                    />
                    <FormControl fullWidth>
                      <InputLabel>Backup Frequency</InputLabel>
                      <Select
                        value={settings.backup}
                        label="Backup Frequency"
                        name="backup"
                        onChange={handleChange}
                      >
                        <MenuItem value="daily">Daily</MenuItem>
                        <MenuItem value="weekly">Weekly</MenuItem>
                        <MenuItem value="monthly">Monthly</MenuItem>
                      </Select>
                    </FormControl>
                  </Stack>
                </CardContent>
              </Card>
            </Grid>
          </Grid>
        </TabPanel>

        <Box sx={{ p: 2, display: 'flex', justifyContent: 'flex-end' }}>
          <Button
            variant="contained"
            startIcon={<SaveIcon />}
            onClick={handleSave}
          >
            Save Changes
          </Button>
        </Box>
      </Paper>
    </Box>
  );
};

export default Settings;

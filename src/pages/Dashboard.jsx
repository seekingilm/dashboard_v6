import React, {useState, useEffect} from 'react';
import {
  Grid,
  Paper,
  Typography,
  Box,
  Card,
  CardContent,
  Avatar,
  List,
  ListItem,
  ListItemAvatar,
  ListItemText,
  ListItemSecondaryAction,
  Chip,
  Divider,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from '@mui/material';
import {
  AttachMoney as AttachMoneyIcon,
  ShoppingCart as ShoppingCartIcon,
  Person as PersonIcon,
  Visibility as VisibilityIcon,
  ArrowUpward as ArrowUpwardIcon,
  ArrowDownward as ArrowDownwardIcon,
  TrendingUp as TrendingUpIcon,
  TrendingDown as TrendingDownIcon,
} from '@mui/icons-material';
import { ResponsiveLine } from '@nivo/line';
import { ResponsivePie } from '@nivo/pie';
import { ResponsiveBar } from '@nivo/bar';

// Sample data for charts
const lineData = [
  {
    id: 'sales',
    color: 'hsl(210, 70%, 50%)',
    data: [
      { x: 'Jan', y: 45 },
      { x: 'Feb', y: 52 },
      { x: 'Mar', y: 48 },
      { x: 'Apr', y: 61 },
      { x: 'May', y: 55 },
      { x: 'Jun', y: 67 },
      { x: 'Jul', y: 71 },
    ],
  },
];

const pieData = [
  { id: 'Electronics', value: 35, color: 'hsl(210, 70%, 50%)' },
  { id: 'Clothing', value: 25, color: 'hsl(180, 70%, 50%)' },
  { id: 'Books', value: 20, color: 'hsl(150, 70%, 50%)' },
  { id: 'Home', value: 15, color: 'hsl(120, 70%, 50%)' },
  { id: 'Other', value: 5, color: 'hsl(90, 70%, 50%)' },
];

const barData2 = [
  { month: 'Jan', new: 45, returning: 28 },
  { month: 'Feb', new: 52, returning: 32 },
  { month: 'Mar', new: 49, returning: 35 },
  { month: 'Apr', new: 62, returning: 42 },
  { month: 'May', new: 58, returning: 45 },
  { month: 'Jun', new: 71, returning: 52 },
];

const salesData = [
  {
    id: 'sales',
    data: [
      { x: 'Jan', y: 45 },
      { x: 'Feb', y: 52 },
      { x: 'Mar', y: 49 },
      { x: 'Apr', y: 62 },
      { x: 'May', y: 58 },
      { x: 'Jun', y: 71 },
    ],
  },
];

const customerSegmentData = [
  { id: 'Electronics', value: 35 },
  { id: 'Clothing', value: 25 },
  { id: 'Food', value: 20 },
  { id: 'Books', value: 15 },
  { id: 'Other', value: 5 },
];

const recentOrders = [
  { id: 1, customer: 'John Doe', product: 'Product A', amount: 100, status: 'Completed', date: '2022-01-01' },
  { id: 2, customer: 'Jane Doe', product: 'Product B', amount: 200, status: 'Processing', date: '2022-01-02' },
  { id: 3, customer: 'John Smith', product: 'Product C', amount: 300, status: 'Completed', date: '2022-01-03' },
];

const topProducts = [
  { name: 'Product A', sales: 100, revenue: 10000, growth: 10 },
  { name: 'Product B', sales: 200, revenue: 20000, growth: -5 },
  { name: 'Product C', sales: 300, revenue: 30000, growth: 15 },
];

const Dashboard = () => {
  const [barData, setBarData] = useState([]);
  const [barData2, setBarData2] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/bar1', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      }
    }).then(res => res.json()).
      then(res => {
        if (res.constructor === Array) {
          setBarData(res)
        }
      })
  }, [])
 
  useEffect(() => {
    fetch('http://127.0.0.1:5000/bar2', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      }
    }).then(res => res.json()).
      then(res => {
        if (res.constructor === Array) {
          setBarData2(res)
        }
      })
  }, [])

  const StatCard = ({ title, value, icon, trend, subtitle }) => (
    <Card>
      <CardContent>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 1 }}>
          <Typography variant="h6" color="text.secondary">
            {title}
          </Typography>
          {icon}
        </Box>
        <Typography variant="h4" component="div" sx={{ mb: 1 }}>
          {value}
        </Typography>
        <Box sx={{ display: 'flex', alignItems: 'center' }}>
          {trend > 0 ? (
            <ArrowUpwardIcon color="success" sx={{ mr: 1 }} />
          ) : (
            <ArrowDownwardIcon color="error" sx={{ mr: 1 }} />
          )}
          <Typography
            variant="body2"
            color={trend > 0 ? 'success.main' : 'error.main'}
          >
            {Math.abs(trend)}% {trend > 0 ? 'increase' : 'decrease'}
          </Typography>
          <Typography variant="body2" color="text.secondary" sx={{ ml: 1 }}>
            {subtitle}
          </Typography>
        </Box>
      </CardContent>
    </Card>
  );

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Dashboard Overview
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Paper sx={{ p: 2, height: 400, width: 1000}}>
            <Typography variant="h6" gutterBottom>
              Role Vs How They Found
            </Typography>
            <Box sx={{ height: 350 }}>
              <ResponsiveBar
                data={barData}
                keys={['family', 'news', 'parent', 'phone', 'tv', 'unknown']}
                indexBy="role"
                margin={{ top: 20, right: 130, bottom: 50, left: 60 }}
                padding={0.3}
                valueScale={{ type: 'linear' }}
                indexScale={{ type: 'band', round: true }}
                colors={{ scheme: 'nivo' }}
                axisTop={null}
                axisRight={null}
                axisBottom={{
                  tickSize: 5,
                  tickPadding: 5,
                  tickRotation: 0,
                }}
                axisLeft={{
                  tickSize: 5,
                  tickPadding: 5,
                  tickRotation: 0,
                }}
                labelSkipWidth={12}
                labelSkipHeight={12}
                legends={[
                  {
                    dataFrom: 'keys',
                    anchor: 'bottom-right',
                    direction: 'column',
                    justify: false,
                    translateX: 120,
                    translateY: 0,
                    itemsSpacing: 2,
                    itemWidth: 100,
                    itemHeight: 20,
                    itemDirection: 'left-to-right',
                    itemOpacity: 0.85,
                    symbolSize: 20,
                  },
                ]}
              />
            </Box>
            <Box sx={{ height: 350 }}>
              <ResponsiveBar
                data={barData2}
                keys={['family', 'cell_words', 'parent', 'alert', 'tv', 'unknown']}
                indexBy="role"
                margin={{ top: 20, right: 130, bottom: 50, left: 60 }}
                padding={0.3}
                valueScale={{ type: 'linear' }}
                indexScale={{ type: 'band', round: true }}
                colors={{ scheme: 'nivo' }}
                axisTop={null}
                axisRight={null}
                axisBottom={{
                  tickSize: 5,
                  tickPadding: 5,
                  tickRotation: 0,
                }}
                axisLeft={{
                  tickSize: 5,
                  tickPadding: 5,
                  tickRotation: 0,
                }}
                labelSkipWidth={12}
                labelSkipHeight={12}
                legends={[
                  {
                    dataFrom: 'keys',
                    anchor: 'bottom-right',
                    direction: 'column',
                    justify: false,
                    translateX: 120,
                    translateY: 0,
                    itemsSpacing: 2,
                    itemWidth: 100,
                    itemHeight: 20,
                    itemDirection: 'left-to-right',
                    itemOpacity: 0.85,
                    symbolSize: 20,
                  },
                ]}
              />
            </Box>
          </Paper>
        </Grid>
<Grid item xs={12}>
          <Paper sx={{ p: 2, height: 400, width: 1000}}>
            <Typography variant="h6" gutterBottom>
              Empty 
            </Typography>
            <Box sx={{ height: 350 }}>
              <ResponsiveBar
                data={[]}
                margin={{ top: 20, right: 130, bottom: 50, left: 60 }}
                padding={0.3}
                valueScale={{ type: 'linear' }}
                indexScale={{ type: 'band', round: true }}
                colors={{ scheme: 'nivo' }}
                axisTop={null}
                axisRight={null}
                axisBottom={{
                  tickSize: 5,
                  tickPadding: 5,
                  tickRotation: 0,
                }}
                axisLeft={{
                  tickSize: 5,
                  tickPadding: 5,
                  tickRotation: 0,
                }}
                labelSkipWidth={12}
                labelSkipHeight={12}
                legends={[
                  {
                    dataFrom: 'keys',
                    anchor: 'bottom-right',
                    direction: 'column',
                    justify: false,
                    translateX: 120,
                    translateY: 0,
                    itemsSpacing: 2,
                    itemWidth: 100,
                    itemHeight: 20,
                    itemDirection: 'left-to-right',
                    itemOpacity: 0.85,
                    symbolSize: 20,
                  },
                ]}
              />
            </Box>
          </Paper>
        </Grid>

      </Grid>
    </Box>
  );
};

export default Dashboard;

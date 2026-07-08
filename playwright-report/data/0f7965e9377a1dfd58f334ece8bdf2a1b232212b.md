# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: opticrop.spec.js >> test
- Location: tests\opticrop.spec.js:12:5

# Error details

```
Test timeout of 30000ms exceeded.
```

```
Error: expect(locator).toBeVisible() failed

Locator: getByText(/muskmelon/i)
Expected: visible
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 5000ms
  - waiting for getByText(/muskmelon/i)

```

```yaml
- text: 🌱
- heading " OptiCrop AI" [level=1]
- paragraph: Smart Agricultural Production Optimization Engine
- heading " Soil & Climate Parameters" [level=2]
- text: Nitrogen (N)
- spinbutton: "100.0"
- text: Phosphorus (P)
- spinbutton: "60.0"
- text: Potassium (K)
- spinbutton: "60.0"
- text: Temperature (°C)
- spinbutton: "35.0"
- text: Humidity (%)
- spinbutton: "70.0"
- text: Soil pH
- spinbutton: "7.0"
- text: Rainfall (mm)
- spinbutton: "200.0"
- button " Analyze & Recommend"
- heading "AI Recommendation" [level=2]
- text: 🌾 coffee Confidence 29.0 % 
- heading "Water Requirement" [level=3]
- paragraph: Moderate
- text: 
- heading "Suitable Soil" [level=3]
- paragraph: Acidic Loamy Soil
- text: 
- heading "Fertilizer" [level=3]
- paragraph: Organic Compost
- text: 
- heading "Cultivation Tip" [level=3]
- paragraph: Grow under partial shade.
```

# Test source

```ts
  1  | test('get started link', async ({ page }) => {
  2  |   await page.goto('https://playwright.dev/');
  3  | 
  4  |   // Click the get started link.
  5  |   await page.getByRole('link', { name: 'Get started' }).click();
  6  | 
  7  |   // Expects page to have a heading with the name of Installation.
  8  |   await expect(page.getByRole('heading', { name: 'Installation' })).toBeVisible();
  9  | });
  10 | import { test, expect } from '@playwright/test';
  11 | 
  12 | test('test', async ({ page }) => {
  13 |   await page.goto('http://127.0.0.1:5000/');
  14 |   await page.getByPlaceholder('Example: 90').click();
  15 |   await page.getByPlaceholder('Example: 90').fill('100');
  16 |   await page.getByPlaceholder('Example: 42').click();
  17 |   await page.getByPlaceholder('Example: 42').fill('60');
  18 |   await page.getByPlaceholder('Example: 43').click();
  19 |   await page.getByPlaceholder('Example: 43').fill('60');
  20 |   await page.getByPlaceholder('Example: 25.5').click();
  21 |   await page.getByPlaceholder('Example: 25.5').fill('35');
  22 |   await page.getByPlaceholder('Example: 82').click();
  23 |   await page.getByPlaceholder('Example: 82').fill('70');
  24 |   await page.getByPlaceholder('- 14').click();
  25 |   await page.getByPlaceholder('- 14').fill('7');
  26 |   await page.getByPlaceholder('Example: 180').click();
  27 |   await page.getByPlaceholder('Example: 180').fill('200');
  28 |   await page.getByRole('button', { name: ' Analyze & Recommend' }).click();
> 29 |   await expect(page.getByText(/muskmelon/i)).toBeVisible();
     |                                              ^ Error: expect(locator).toBeVisible() failed
  30 |   await page.getByPlaceholder('Example: 180').click();
  31 |   await page.getByPlaceholder('Example: 180').click();
  32 |   await page.getByPlaceholder('Example: 180').fill('180');
  33 |   await page.getByPlaceholder('Example: 42').click();
  34 |   await page.getByPlaceholder('Example: 42').fill('100');
  35 |   await page.getByPlaceholder('Example: 43').click();
  36 |   await page.getByPlaceholder('Example: 43').fill('100');
  37 |   await page.getByPlaceholder('Example: 25.5').click();
  38 |   await page.getByPlaceholder('Example: 25.5').fill('32');
  39 |   await page.getByPlaceholder('Example: 82').click();
  40 |   await page.getByPlaceholder('Example: 82').fill('50');
  41 |   await page.getByPlaceholder('- 14').click();
  42 |   await page.getByPlaceholder('- 14').fill('8');
  43 |   await page.getByRole('button', { name: ' Analyze & Recommend' }).click();
  44 |   await page.getByText('AI Recommendation 🌾 banana').click();
  45 |   await page.getByPlaceholder('Example: 90').click();
  46 |   await page.getByPlaceholder('Example: 90').fill('50');
  47 |   await page.getByPlaceholder('Example: 42').click();
  48 |   await page.getByPlaceholder('Example: 42').fill('50');
  49 |   await page.getByPlaceholder('Example: 180').click();
  50 |   await page.getByPlaceholder('Example: 180').fill('100');
  51 |   await page.getByRole('button', { name: ' Analyze & Recommend' }).click();
  52 |   await page.getByText('AI Recommendation 🌾 mango').click();
  53 |   await page.locator('div').nth(5).click();
  54 |   await page.getByPlaceholder('Example: 43').click();
  55 |   await page.getByPlaceholder('Example: 43').fill('50');
  56 |   await page.getByPlaceholder('Example: 180').click();
  57 |   await page.getByPlaceholder('Example: 180').fill('300');
  58 |   await page.getByRole('button', { name: ' Analyze & Recommend' }).click();
  59 |   await page.locator('div').nth(5).click();
  60 | });
```
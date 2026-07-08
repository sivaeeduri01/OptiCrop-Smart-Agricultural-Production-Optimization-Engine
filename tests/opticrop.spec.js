test('get started link', async ({ page }) => {
  await page.goto('https://playwright.dev/');

  // Click the get started link.
  await page.getByRole('link', { name: 'Get started' }).click();

  // Expects page to have a heading with the name of Installation.
  await expect(page.getByRole('heading', { name: 'Installation' })).toBeVisible();
});
import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://127.0.0.1:5000/');
  await page.getByPlaceholder('Example: 90').click();
  await page.getByPlaceholder('Example: 90').fill('100');
  await page.getByPlaceholder('Example: 42').click();
  await page.getByPlaceholder('Example: 42').fill('60');
  await page.getByPlaceholder('Example: 43').click();
  await page.getByPlaceholder('Example: 43').fill('60');
  await page.getByPlaceholder('Example: 25.5').click();
  await page.getByPlaceholder('Example: 25.5').fill('35');
  await page.getByPlaceholder('Example: 82').click();
  await page.getByPlaceholder('Example: 82').fill('70');
  await page.getByPlaceholder('- 14').click();
  await page.getByPlaceholder('- 14').fill('7');
  await page.getByPlaceholder('Example: 180').click();
  await page.getByPlaceholder('Example: 180').fill('200');
  await page.getByRole('button', { name: ' Analyze & Recommend' }).click();
  await expect(page.getByText(/muskmelon/i)).toBeVisible();
  await page.getByPlaceholder('Example: 180').click();
  await page.getByPlaceholder('Example: 180').click();
  await page.getByPlaceholder('Example: 180').fill('180');
  await page.getByPlaceholder('Example: 42').click();
  await page.getByPlaceholder('Example: 42').fill('100');
  await page.getByPlaceholder('Example: 43').click();
  await page.getByPlaceholder('Example: 43').fill('100');
  await page.getByPlaceholder('Example: 25.5').click();
  await page.getByPlaceholder('Example: 25.5').fill('32');
  await page.getByPlaceholder('Example: 82').click();
  await page.getByPlaceholder('Example: 82').fill('50');
  await page.getByPlaceholder('- 14').click();
  await page.getByPlaceholder('- 14').fill('8');
  await page.getByRole('button', { name: ' Analyze & Recommend' }).click();
  await page.getByText('AI Recommendation 🌾 banana').click();
  await page.getByPlaceholder('Example: 90').click();
  await page.getByPlaceholder('Example: 90').fill('50');
  await page.getByPlaceholder('Example: 42').click();
  await page.getByPlaceholder('Example: 42').fill('50');
  await page.getByPlaceholder('Example: 180').click();
  await page.getByPlaceholder('Example: 180').fill('100');
  await page.getByRole('button', { name: ' Analyze & Recommend' }).click();
  await page.getByText('AI Recommendation 🌾 mango').click();
  await page.locator('div').nth(5).click();
  await page.getByPlaceholder('Example: 43').click();
  await page.getByPlaceholder('Example: 43').fill('50');
  await page.getByPlaceholder('Example: 180').click();
  await page.getByPlaceholder('Example: 180').fill('300');
  await page.getByRole('button', { name: ' Analyze & Recommend' }).click();
  await page.locator('div').nth(5).click();
});
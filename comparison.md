```
goos: linux
goarch: amd64
pkg: github.com/casbin/pycasbin
cpu: GitHub Actions Runner

                                                  │   old base.json   │   new pr.json                │
                                                  │    sec/op     │    sec/op     │
ABACModel                                          23.76us ± 1%    21.96us ± 1%        -7.58% ➡️
ABACRuleModel                                      34.40ms ± 1%    35.08ms ± 1%        +1.98% ➡️
AddPolicyLarge                                     204.72us ± 1%   254.54us ± 1%       +24.34% 🐌
AddPolicyMedium                                    540.42us ± 1%   537.57us ± 1%       -0.53% ➡️
AddPolicySmall                                     11.54us ± 1%    12.28us ± 1%        +6.41% ➡️
BasicModel                                         28.04us ± 1%    27.43us ± 1%        -2.18% ➡️
BuildRoleLinksWithDomainPatternLarge               5.60ms ± 1%     5.67ms ± 1%         +1.25% ➡️
BuildRoleLinksWithPatternAndDomainPatternLarge     5.86ms ± 1%     5.86ms ± 1%         +0.00% ➡️
BuildRoleLinksWithPatternLarge                     4.80ms ± 1%     5.03ms ± 1%         +4.79% ➡️
ExtractTokensLongNested                            3.32us ± 1%     3.25us ± 1%         -2.11% ➡️
ExtractTokensLongSimple                            1.64us ± 1%     1.73us ± 1%         +5.49% ➡️
ExtractTokensShortNested                           2.42us ± 1%     2.41us ± 1%         -0.41% ➡️
ExtractTokensShortSimple                           1.50us ± 1%     1.39us ± 1%         -7.33% ➡️
Globmatch                                          88.09us ± 1%    83.36us ± 1%        -5.37% ➡️
HasLinkWithDomainPatternLarge                      2.95us ± 1%     3.24us ± 1%         +9.83% ➡️
HasLinkWithPatternAndDomainPatternLarge            2.09us ± 1%     2.24us ± 1%         +7.18% ➡️
HasLinkWithPatternLarge                            4.17us ± 1%     3.73us ± 1%         -10.55% 🚀
HasPolicyLarge                                     77.10us ± 1%    72.65us ± 1%        -5.77% ➡️
HasPolicyMedium                                    8.49us ± 1%     8.60us ± 1%         +1.30% ➡️
HasPolicySmall                                     2.40us ± 1%     2.22us ± 1%         -7.50% ➡️
KeyMatchModel                                      41.50us ± 1%    35.55us ± 1%        -14.34% 🚀
PriorityModel                                      39.17us ± 1%    32.89us ± 1%        -16.03% 🚀
Raw                                                205.15ns ± 1%   205.83ns ± 1%       +0.33% ➡️
RBACModel                                          33.68us ± 1%    32.41us ± 1%        -3.77% ➡️
RBACModelLarge                                     37.58ms ± 1%    37.39ms ± 1%        -0.51% ➡️
RBACModelMedium                                    3.60ms ± 1%     3.55ms ± 1%         -1.39% ➡️
RBACModelSizesLarge                                455.81ms ± 1%   494.18ms ± 1%       +8.42% ➡️
RBACModelSizesMedium                               43.49ms ± 1%    41.72ms ± 1%        -4.07% ➡️
RBACModelSizesSmall                                4.72ms ± 1%     5.30ms ± 1%         +12.29% 🐌
RBACModelSmall                                     375.24us ± 1%   399.18us ± 1%       +6.38% ➡️
RBACModelWithDomains                               42.89us ± 1%    40.54us ± 1%        -5.48% ➡️
RBACModelWithDomainsPatternLarge                   2.54ms ± 1%     70.34us ± 1%        -97.23% 🚀
RBACModelWithResourceRoles                         56.39us ± 1%    55.86us ± 1%        -0.94% ➡️
RBACWithDeny                                       55.21us ± 1%    54.56us ± 1%        -1.18% ➡️
RemovePolicyLarge                                  71.85us ± 1%    72.76us ± 1%        +1.27% ➡️
RemovePolicyMedium                                 9.20us ± 1%     9.01us ± 1%         -2.07% ➡️
RemovePolicySmall                                  2.53us ± 1%     2.62us ± 1%         +3.56% ➡️
RoleManagerLarge                                   8.63ms ± 1%     7.44ms ± 1%         -13.79% 🚀
RoleManagerMedium                                  1.03ms ± 1%     1.08ms ± 1%         +4.85% ➡️
RoleManagerSmall                                   64.50us ± 1%    68.70us ± 1%        +6.51% ➡️
geomean                                            110.60us        100.65us            -9.00% ➡️
```

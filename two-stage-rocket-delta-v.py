import math

gravity_acceleration = 9.80665

stage_one_specific_impulse = 250
stage_two_specific_impulse = 317

stage_one_burnout_weight_ratio = 0.15
stage_two_burnout_weight_ratio = 0.045

# wet mass include other stages and payload
stage_one_wet_mass = 100000
stage_two_wet_mass = 29000
payload_mass = 1650

# burnout mass does not include other stages and payload. It is the stage dry mass plus ullage
stage_one_burnout_mass = (stage_one_wet_mass - stage_two_wet_mass) * stage_one_burnout_weight_ratio
stage_two_burnout_mass = (stage_two_wet_mass - payload_mass) * stage_two_burnout_weight_ratio


def delta_v():
    stage_one_delta_v = stage_one_specific_impulse * gravity_acceleration * math.log(stage_one_wet_mass / (stage_two_wet_mass + stage_one_burnout_mass))

    stage_two_delta_v = stage_two_specific_impulse * gravity_acceleration * math.log(stage_two_wet_mass / (payload_mass + stage_two_burnout_mass))

    final_delta_v = stage_two_delta_v + stage_one_delta_v

    print("Delta-v of stage one: %.2f m/s" % stage_one_delta_v)
    print("Delta-v of stage two: %.2f m/s" % stage_two_delta_v)
    print("Final delta-V: %.2f m/s" % final_delta_v)


delta_v()

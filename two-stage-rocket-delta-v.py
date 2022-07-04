import math
import matplotlib.pyplot as plot
import numpy

gravity_acceleration = 9.80665


def delta_v(
        stage_two_wet_mass_ratio,
        payload_mass_ratio,
        stage_one_specific_impulse,
        stage_two_specific_impulse,
        stage_one_burnout_ratio,
        stage_two_burnout_ratio
):

    stage_one_wet_mass_ratio = 1

    # burnout mass is the stage dry mass plus ullage. Does not include stage or payloads above
    stage_one_burnout_mass_ratio = (stage_one_wet_mass_ratio - stage_two_wet_mass_ratio) * stage_one_burnout_ratio
    stage_two_burnout_mass_ratio = (stage_two_wet_mass_ratio - payload_mass_ratio) * stage_two_burnout_ratio

    stage_one_delta_v = stage_one_specific_impulse * gravity_acceleration * math.log(
        stage_one_wet_mass_ratio / (stage_two_wet_mass_ratio + stage_one_burnout_mass_ratio))

    stage_two_delta_v = stage_two_specific_impulse * gravity_acceleration * math.log(
        stage_two_wet_mass_ratio / (payload_mass_ratio + stage_two_burnout_mass_ratio))

    final_delta_v = stage_two_delta_v + stage_one_delta_v

    return final_delta_v


def delta_v_vs_stage_two_wet_mass_ratio_graph():
    stage_one_specific_impulse = 250
    stage_two_specific_impulse = 317

    # burnout ratio is the stage dry ratio plus ullage ratio. Does not include stage or payloads above
    stage_one_burnout_ratio = 0.15
    stage_two_burnout_ratio = 0.045

    # wet mass include other stages and payload
    stage_two_wet_mass_ratio_values = numpy.arange(0.2, 0.4, 0.005)
    payload_mass_ratio = 0.0165

    delta_v_values = []

    for stage_two_wet_mass_ratio in stage_two_wet_mass_ratio_values:
        value = delta_v(
            stage_two_wet_mass_ratio,
            payload_mass_ratio,
            stage_one_specific_impulse,
            stage_two_specific_impulse,
            stage_one_burnout_ratio,
            stage_two_burnout_ratio
        )

        delta_v_values.append(value)

    # plotting the points
    plot.plot(stage_two_wet_mass_ratio_values, delta_v_values)

    plot.xlabel('Stage Two Wet Mass Ratio')
    plot.ylabel('Delta-V [m/s]')
    plot.title('Delta-V VS Stage Two Wet Mass Ratio')

    # function to show the plot
    plot.show()


delta_v_vs_stage_two_wet_mass_ratio_graph()
